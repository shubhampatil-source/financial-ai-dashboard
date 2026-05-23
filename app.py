import streamlit as st
import pandas as pd

# ---------------------------------------------------
# UTILITY IMPORTS
# ---------------------------------------------------

from utils.data_loader import load_data
from utils.data_cleaner import clean_financial_data
from utils.kpi_engine import calculate_kpis

from utils.charts import (
    revenue_chart,
    profit_chart
)

from utils.dynamic_chart import dynamic_metric_chart

from utils.forecasting import revenue_forecast

from utils.anomaly_detection import detect_anomalies

from utils.report_generator import generate_pdf_report

from utils.unified_pipeline import process_financial_pdf

from utils.rag_engine import (
    chunk_text,
    create_vector_store,
    retrieve_relevant_chunks
)

from utils.ai_engine import (
    generate_financial_insights,
    financial_chat,
    analyze_pdf_report,
    rag_financial_chat,
    executive_summary,
    detect_financial_risks
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Financial Dashboard",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: white;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #333333;
}

div[data-testid="stSidebar"] {
    background-color: #161A23;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "latest_ai_report" not in st.session_state:
    st.session_state.latest_ai_report = ""

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Financial AI Dashboard")

selected_metric = st.sidebar.selectbox(
    "Select Financial Metric",
    [
        "Revenue",
        "Expenses",
        "Net_Profit",
        "Assets",
        "Liabilities"
    ]
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("AI Financial Storytelling Dashboard")

st.write(
    "Upload financial statements and analyze KPIs using AI."
)

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload Financial Files",
    type=["csv", "xlsx", "pdf"],
    accept_multiple_files=True
)

# ---------------------------------------------------
# PROCESS FILES
# ---------------------------------------------------

if uploaded_files:

    for uploaded_file in uploaded_files:

        # ===================================================
        # PDF PIPELINE
        # ===================================================

        if uploaded_file.name.endswith(".pdf"):

            st.header(
                f"PDF Intelligence — {uploaded_file.name}"
            )

            try:

                # ------------------------------------------
                # UNIFIED PIPELINE
                # ------------------------------------------

                financial_df, pdf_text = (
                    process_financial_pdf(
                        uploaded_file
                    )
                )

                # ------------------------------------------
                # PDF TEXT
                # ------------------------------------------

                with st.expander(
                    "View Extracted PDF Text"
                ):

                    st.text_area(
                        "PDF Text",
                        pdf_text[:5000],
                        height=300
                    )

                # ------------------------------------------
                # STRUCTURED DATA
                # ------------------------------------------

                st.subheader(
                    "Extracted Financial Metrics"
                )

                st.dataframe(financial_df)

                # ------------------------------------------
                # KPI SECTION
                # ------------------------------------------

                if not financial_df.empty:

                    kpis = calculate_kpis(
                        financial_df
                    )

                    st.subheader(
                        "Financial KPIs"
                    )

                    col1, col2, col3 = (
                        st.columns(3)
                    )

                    col1.metric(
                        "Revenue Growth %",
                        f"{kpis['Revenue Growth %']}%"
                    )

                    col2.metric(
                        "Profit Margin %",
                        f"{kpis['Profit Margin %']}%"
                    )

                    col3.metric(
                        "Current Ratio",
                        kpis['Current Ratio']
                    )

                    # ------------------------------------------
                    # CHARTS
                    # ------------------------------------------

                    if "Year" in financial_df.columns:

                        st.subheader("Revenue Trend")

                        st.plotly_chart(
                            revenue_chart(financial_df),
                            use_container_width=True
                        )

                        st.subheader("Profit Trend")

                        st.plotly_chart(
                            profit_chart(financial_df),
                            use_container_width=True
                        )

                    else:

                        st.info(
                            """
                    Charts require multi-year financial data.

                    Current PDF extraction detected
                    single-period financial metrics only.
                    """
                        )

                # ------------------------------------------
                # RAG ENGINE
                # ------------------------------------------

                chunks = chunk_text(pdf_text)

                index, embeddings = (
                    create_vector_store(chunks)
                )

                # ------------------------------------------
                # PDF AI ANALYSIS
                # ------------------------------------------

                st.subheader(
                    "AI PDF Analysis"
                )

                if st.button(
                    f"Analyze PDF {uploaded_file.name}"
                ):

                    with st.spinner(
                        "Analyzing report..."
                    ):

                        pdf_analysis = (
                            analyze_pdf_report(
                                pdf_text
                            )
                        )

                        st.write(pdf_analysis)

                # ------------------------------------------
                # PDF RAG Q&A
                # ------------------------------------------

                st.subheader(
                    "Ask Questions About PDF"
                )

                pdf_question = st.text_input(
                    "Ask question about report",
                    key=f"pdf_question_{uploaded_file.name}"
                )

                if st.button(
                    f"Ask PDF AI {uploaded_file.name}"
                ):

                    with st.spinner("Creating AI search index..."):

                        chunks = chunk_text(pdf_text)

                        index, embeddings = create_vector_store(
                            chunks
                        )

                        relevant_chunks = (
                            retrieve_relevant_chunks(
                                pdf_question,
                                chunks,
                                index
                            )
                        )

                        rag_answer = rag_financial_chat(
                            pdf_question,
                            relevant_chunks
                        )

                        st.write(rag_answer)

            except Exception as e:

                st.error(
                    f"PDF Processing Error: {e}"
                )

        # ===================================================
        # CSV / XLSX PIPELINE
        # ===================================================

        else:

            st.header(
                f"Financial Dashboard — {uploaded_file.name}"
            )

            try:

                # ------------------------------------------
                # LOAD DATA
                # ------------------------------------------

                df = load_data(uploaded_file)

                df = clean_financial_data(df)

                # ------------------------------------------
                # VALIDATION
                # ------------------------------------------

                required_columns = [
                    "Revenue",
                    "Net_Profit",
                    "Assets",
                    "Liabilities"
                ]

                missing_columns = [
                    col
                    for col in required_columns
                    if col not in df.columns
                ]

                if missing_columns:

                    st.error(
                        f"Missing columns: {missing_columns}"
                    )

                    continue

                # ------------------------------------------
                # DATA PREVIEW
                # ------------------------------------------

                st.subheader("Financial Data")

                st.dataframe(df)

                # ------------------------------------------
                # KPI CALCULATIONS
                # ------------------------------------------

                kpis = calculate_kpis(df)

                # ------------------------------------------
                # FINANCIAL CONTEXT
                # ------------------------------------------

                financial_context = f"""

                Revenue Growth:
                {kpis['Revenue Growth %']}%

                Profit Margin:
                {kpis['Profit Margin %']}%

                Current Ratio:
                {kpis['Current Ratio']}

                Financial Data:
                {df.to_string(index=False)}

                """

                # ------------------------------------------
                # KPI SECTION
                # ------------------------------------------

                st.subheader("Financial KPIs")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Revenue Growth %",
                    f"{kpis['Revenue Growth %']}%"
                )

                col2.metric(
                    "Profit Margin %",
                    f"{kpis['Profit Margin %']}%"
                )

                col3.metric(
                    "Current Ratio",
                    kpis['Current Ratio']
                )

                # ------------------------------------------
                # VISUALIZATION
                # ------------------------------------------

                st.subheader(
                    "Financial Visualization"
                )

                st.plotly_chart(
                    dynamic_metric_chart(
                        df,
                        selected_metric
                    ),
                    use_container_width=True
                )

                # ------------------------------------------
                # ANOMALY DETECTION
                # ------------------------------------------

                st.subheader(
                    "Revenue Anomaly Detection"
                )

                anomalies = detect_anomalies(df)

                if anomalies.empty:

                    st.success(
                        "No major anomalies detected."
                    )

                else:

                    st.warning(
                        "Potential anomalies detected."
                    )

                    st.dataframe(anomalies)

                # ------------------------------------------
                # FORECASTING
                # ------------------------------------------

                if len(df) >= 3:

                    st.subheader(
                        "Revenue Forecast"
                    )

                    forecast = revenue_forecast(df)

                    st.line_chart(
                        forecast[
                            ['ds', 'yhat']
                        ].set_index('ds')
                    )

                # ------------------------------------------
                # AI INSIGHTS
                # ------------------------------------------

                st.subheader(
                    "AI Financial Insights"
                )

                if st.button(
                    f"Generate Insights {uploaded_file.name}"
                ):

                    with st.spinner(
                        "Generating AI insights..."
                    ):

                        insights = (
                            generate_financial_insights(
                                kpis
                            )
                        )

                        st.session_state.latest_ai_report = insights

                        st.write(insights)

                # ------------------------------------------
                # DOWNLOAD REPORT
                # ------------------------------------------

                if st.session_state.latest_ai_report:

                    if st.button(
                        f"Generate PDF Report {uploaded_file.name}"
                    ):

                        generate_pdf_report(
                            st.session_state.latest_ai_report
                        )

                        with open(
                            "financial_report.pdf",
                            "rb"
                        ) as file:

                            st.download_button(
                                label="Download Report",
                                data=file,
                                file_name="financial_report.pdf",
                                mime="application/pdf"
                            )

                # ------------------------------------------
                # EXECUTIVE SUMMARY
                # ------------------------------------------

                st.subheader(
                    "Executive Summary"
                )

                if st.button(
                    f"Executive Summary {uploaded_file.name}"
                ):

                    summary = executive_summary(
                        financial_context
                    )

                    st.write(summary)

                # ------------------------------------------
                # RISK DETECTION
                # ------------------------------------------

                st.subheader(
                    "AI Risk Detection"
                )

                if st.button(
                    f"Risk Detection {uploaded_file.name}"
                ):

                    risks = detect_financial_risks(
                        kpis
                    )

                    st.write(risks)

                # ------------------------------------------
                # AI CHATBOT
                # ------------------------------------------

                st.subheader(
                    "AI Financial Chat"
                )

                user_question = st.text_input(
                    "Ask financial question",
                    key=f"chat_{uploaded_file.name}"
                )

                if st.button(
                    f"Ask AI {uploaded_file.name}"
                ):

                    if user_question.strip() != "":

                        answer = financial_chat(
                            user_question,
                            financial_context
                        )

                        st.session_state.chat_history.append(
                            {
                                "question": user_question,
                                "answer": answer
                            }
                        )

                # ------------------------------------------
                # CHAT HISTORY
                # ------------------------------------------

                if st.session_state.chat_history:

                    st.subheader("Chat History")

                    for chat in reversed(
                        st.session_state.chat_history
                    ):

                        st.markdown(
                            f"**Question:** {chat['question']}"
                        )

                        st.markdown(
                            f"**Answer:** {chat['answer']}"
                        )

                        st.divider()

            except Exception as e:

                st.error(
                    f"Application Error: {e}"
                )
