
import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# --------------------------------------------------
# CIGNA QUOTEFLOW AI — STREAMLIT PROTOTYPE
# --------------------------------------------------

st.set_page_config(
    page_title="QuoteFlow AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM DESIGN -------------------

st.markdown("""
<style>
.stApp {
    background-color: #08111f;
    color: #f0f6ff;
}
[data-testid="stSidebar"] {
    background-color: #101e32;
}
h1, h2, h3 {
    color: #42dfc2 !important;
}
div[data-testid="stMetric"] {
    background: #122139;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #293d56;
}
div[data-testid="stMetricLabel"] {
    color: #a4b4ca;
}
div[data-testid="stMetricValue"] {
    color: #42dfc2;
}
.stButton button {
    border-radius: 9px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION DATA --------------------

if "cases" not in st.session_state:
    st.session_state.cases = pd.DataFrame([
        {
            "Reference": "QF-1042",
            "Company": "Northstar Trading",
            "Type": "SME Health",
            "Status": "New Submission",
            "Created": "2026-10-15"
        },
        {
            "Reference": "QF-1043",
            "Company": "Cedar Works",
            "Type": "SME Health",
            "Status": "Validated",
            "Created": "2026-10-15"
        },
        {
            "Reference": "QF-1044",
            "Company": "Blue Harbor Studio",
            "Type": "SME Health",
            "Status": "Exception Flagged",
            "Created": "2026-10-15"
        }
    ])

if "activity" not in st.session_state:
    st.session_state.activity = [
        "QuoteFlow AI prototype initialized.",
        "Demo cases loaded successfully."
    ]

if "next_id" not in st.session_state:
    st.session_state.next_id = 1045

# ---------------- HEADER --------------------------

st.title("QuoteFlow AI")
st.caption(
    "Intelligent Insurance Quotation Workflow | "
    "Ignyte × Cigna Challenge Concept"
)

st.info(
    "DEMO MODE — This application uses simulated data. "
    "It does not issue insurance quotations or connect to "
    "Cigna, Salesforce, or live insurance systems."
)

# ---------------- SIDEBAR -------------------------

with st.sidebar:
    st.header("Navigation")

    page = st.radio(
        "Select workspace",
        [
            "Dashboard",
            "Document Validation",
            "Quotation Management",
            "Reports & KPIs",
            "Integration Roadmap"
        ]
    )

    st.divider()

    st.caption("QuoteFlow AI")
    st.caption("Prototype v1.0")
    st.caption("Sample data only")

cases = st.session_state.cases

# ---------------- DASHBOARD -----------------------

if page == "Dashboard":

    st.subheader("Executive Dashboard")
    st.write(
        "Monitor quotation intake, processing progress, "
        "and cases requiring additional review."
    )

    total = len(cases)
    validated = int(
        cases["Status"].isin(
            ["Validated", "Underwriting Review",
             "Quotation Prepared", "Completed"]
        ).sum()
    )
    review = int(
        (cases["Status"] == "Underwriting Review").sum()
    )
    exceptions = int(
        (cases["Status"] == "Exception Flagged").sum()
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", total)
    col2.metric("Validated Cases", validated)
    col3.metric("Under Review", review)
    col4.metric("Exceptions", exceptions)

    st.divider()

    left, right = st.columns([1.5, 1])

    with left:
        st.subheader("Quotation Pipeline")

        if not cases.empty:
            status_counts = (
                cases["Status"].value_counts()
                .rename_axis("Status")
                .reset_index(name="Cases")
            )

            st.bar_chart(
                status_counts.set_index("Status")
            )

    with right:
        st.subheader("Case Status")

        if not cases.empty:
            st.dataframe(
                cases[
                    ["Reference", "Company", "Status"]
                ],
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("No cases available.")

    st.subheader("Recent Activity")

    for event in reversed(st.session_state.activity[-8:]):
        st.write("• " + event)

# ---------------- DOCUMENT VALIDATION -------------

elif page == "Document Validation":

    st.subheader("SME Census Validation")

    st.write(
        "Upload a CSV file to check required fields, "
        "missing values, and basic data consistency."
    )

    st.warning(
        "Use fictional sample data only. Do not upload "
        "real customer information or medical records."
    )

    uploaded_file = st.file_uploader(
        "Upload census CSV",
        type=["csv"]
    )

    st.download_button(
        "Download Sample CSV",
        data=(
            "company,employee_id,age,plan\n"
            "Northstar Trading,EMP001,34,Standard\n"
            "Northstar Trading,EMP002,41,Enhanced\n"
            "Northstar Trading,EMP003,29,Standard\n"
        ),
        file_name="sample_census.csv",
        mime="text/csv"
    )

    if uploaded_file is not None:

        try:
            df = pd.read_csv(uploaded_file)

            st.write("### Uploaded Data")
            st.dataframe(
                df.head(100),
                use_container_width=True
            )

            required = [
                "company",
                "employee_id",
                "age",
                "plan"
            ]

            # Normalize column names for validation.
            normalized = {
                str(column).strip().lower(): column
                for column in df.columns
            }

            missing_columns = [
                column for column in required
                if column not in normalized
            ]

            if missing_columns:
                st.error(
                    "Missing required columns: "
                    + ", ".join(missing_columns)
                )

            else:
                issues = []

                for field in required:
                    original = normalized[field]

                    empty = (
                        df[original].isna()
                        | df[original].astype(str).str.strip().eq("")
                    )

                    for index in df.index[empty][:20]:
                        issues.append(
                            f"Row {index + 2}: "
                            f"{field} is missing."
                        )

                age_column = normalized["age"]

                ages = pd.to_numeric(
                    df[age_column],
                    errors="coerce"
                )

                for index in df.index[
                    ages.isna() | (ages < 0) | (ages > 120)
                ][:20]:
                    issues.append(
                        f"Row {index + 2}: "
                        "age must be a number between 0 and 120."
                    )

                st.metric("Records Uploaded", len(df))

                if issues:
                    st.error(
                        f"Found {len(issues)} validation issue(s)."
                    )

                    for issue in issues[:30]:
                        st.write("• " + issue)

                    if len(issues) > 30:
                        st.caption(
                            "Only the first 30 issues are displayed."
                        )

                else:
                    st.success(
                        "Basic structural validation passed."
                    )

                    st.caption(
                        "This does not verify insurance eligibility, "
                        "pricing accuracy, or underwriting approval."
                    )

                st.session_state.activity.append(
                    f"Census validation completed: "
                    f"{len(df)} records, {len(issues)} issue(s)."
                )

        except Exception as error:
            st.error(
                "Could not process the CSV file. "
                "Please check its format and try again."
            )

# ---------------- QUOTATION MANAGEMENT -------------

elif page == "Quotation Management":

    st.subheader("Quotation Case Management")

    st.write("Create a case or update an existing case status.")

    with st.form("new_case_form"):

        company = st.text_input(
            "Company / Customer Name"
        )

        quote_type = st.selectbox(
            "Insurance Product",
            [
                "SME Health",
                "Individual Health",
                "Other"
            ]
        )

        create_case = st.form_submit_button(
            "Create Quotation Case"
        )

        if create_case:

            if not company.strip():
                st.error("Enter a company name.")
            else:
                reference = (
                    f"QF-{st.session_state.next_id}"
                )

                new_case = pd.DataFrame([{
                    "Reference": reference,
                    "Company": company.strip(),
                    "Type": quote_type,
                    "Status": "New Submission",
                    "Created": datetime.now().strftime("%Y-%m-%d")
                }])

                st.session_state.cases = pd.concat(
                    [
                        st.session_state.cases,
                        new_case
                    ],
                    ignore_index=True
                )

                st.session_state.next_id += 1

                st.session_state.activity.append(
                    f"Created demo case {reference}: {company}."
                )

                st.success(
                    f"Created case {reference} successfully."
                )

    st.divider()
    st.subheader("Update Existing Case")

    cases = st.session_state.cases

    if not cases.empty:

        references = cases["Reference"].tolist()

        selected_ref = st.selectbox(
            "Select Case",
            references
        )

        selected = cases[
            cases["Reference"] == selected_ref
        ].iloc[0]

        st.write("**Company:**", selected["Company"])
        st.write("**Product:**", selected["Type"])
        st.write("**Current status:**", selected["Status"])

        statuses = [
            "New Submission",
            "Validated",
            "Underwriting Review",
            "Quotation Prepared",
            "Completed",
            "Exception Flagged"
        ]

        current_status = selected["Status"]

        default_index = (
            statuses.index(current_status)
            if current_status in statuses else 0
        )

        new_status = st.selectbox(
            "New Status",
            statuses,
            index=default_index
        )

        if st.button("Update Case Status"):

            idx = st.session_state.cases.index[
                st.session_state.cases["Reference"]
                == selected_ref
            ][0]

            st.session_state.cases.at[
                idx, "Status"
            ] = new_status

            st.session_state.activity.append(
                f"{selected_ref} status changed to {new_status}."
            )

            st.success("Case status updated.")
            st.rerun()

    st.divider()
    st.subheader("All Quotation Cases")

    st.dataframe(
        st.session_state.cases,
        hide_index=True,
        use_container_width=True
    )

# ---------------- REPORTS -------------------------

elif page == "Reports & KPIs":

    st.subheader("Performance Reports")

    cases = st.session_state.cases

    total = len(cases)

    completed = int(
        (cases["Status"] == "Completed").sum()
    ) if total else 0

    exception_count = int(
        (cases["Status"] == "Exception Flagged").sum()
    ) if total else 0

    completion_rate = (
        completed / total * 100 if total else 0
    )

    exception_rate = (
        exception_count / total * 100 if total else 0
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Cases", total)
    c2.metric("Completed Cases", completed)
    c3.metric("Completion Rate", f"{completion_rate:.1f}%")

    st.write("### Case Distribution")

    if total:
        st.bar_chart(
            cases["Status"].value_counts()
        )

    st.write("### Exception Rate")

    st.progress(
        min(exception_rate / 100, 1.0)
    )

    st.write(f"{exception_rate:.1f}% of demo cases are flagged.")

    csv_data = cases.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Quotation Report",
        data=csv_data,
        file_name="quoteflow_report.csv",
        mime="text/csv"
    )

    st.caption(
        "Metrics describe the current demo cases only. "
        "No real operational performance is being measured."
    )

# ---------------- INTEGRATION ROADMAP -------------

elif page == "Integration Roadmap":

    st.subheader("Proposed Technical Architecture")

    st.write(
        "The following integrations are planned architecture, "
        "not active connections."
    )

    st.markdown("""
    **1. Customer Intake**
    
    Web form and secure bulk CSV upload.
    
    **2. Validation Service**
    
    Required-field checks, file validation, and exception handling.
    
    **3. Workflow Orchestration**
    
    Case routing, status tracking, and human review.
    
    **4. Salesforce CRM Adapter**
    
    Authorized API integration for customer and opportunity records.
    
    **5. Insurance Rating and Policy Systems**
    
    Connect to approved existing systems through documented APIs.
    
    **6. Monitoring and Reporting**
    
    Audit logs, quotation pipeline, turnaround metrics, and exceptions.
    """)

    st.warning(
        "Before production, implement authentication, role-based access, "
        "encryption, secure secret management, audit logging, "
        "data-residency controls, and a formal compliance review. "
        "Confirm applicable UAE requirements with qualified compliance "
        "and legal specialists."
    )

    st.subheader("Suggested Success Metrics")

    st.table(pd.DataFrame({
        "Metric": [
            "Quotation turnaround time",
            "Manual data-entry rate",
            "Submission completeness",
            "Exception resolution time",
            "Lead-to-quote conversion"
        ],
        "Measurement": [
            "Compare before and after implementation",
            "Measure cases requiring manual re-entry",
            "Measure complete submissions",
            "Track time to resolve flagged cases",
            "Track qualified leads converted to quotes"
        ]
    }))

# ---------------- FOOTER --------------------------

st.divider()

st.caption(
    "QuoteFlow AI | Innovation Challenge Prototype | "
    "Synthetic data only | No live insurer integrations"
)
