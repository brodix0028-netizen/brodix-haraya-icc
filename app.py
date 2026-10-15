
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>QuoteFlow AI | Insurance Automation</title>
<style>
:root {
  --bg:#08111f; --panel:#111f33; --line:#293d56;
  --text:#f0f6ff; --muted:#a4b4ca;
  --teal:#43e0c1; --blue:#6aa9ff; --amber:#ffd078;
}
* { box-sizing:border-box; }
body {
  margin:0; font-family:Arial,sans-serif; background:var(--bg);
  color:var(--text);
}
header {
  padding:20px; border-bottom:1px solid var(--line);
  display:flex; justify-content:space-between; align-items:center;
  gap:12px; flex-wrap:wrap;
}
header h1 { margin:0; font-size:21px; }
header p,.muted { color:var(--muted); font-size:13px; }
.tag { color:var(--teal); font-size:12px; }
main { max-width:1100px; margin:auto; padding:22px 16px; }
h2 { font-size:clamp(27px,5vw,40px); margin-bottom:8px; }
button,select,input {
  font:inherit; border-radius:9px; padding:11px;
}
button { border:0; cursor:pointer; font-weight:bold; }
.primary { background:var(--teal); color:#06201c; }
.secondary {
  background:#203650; color:white; border:1px solid #3a5270;
}
input,select {
  background:#091629; color:white; border:1px solid var(--line);
  width:100%; margin:8px 0;
}
.stats {
  display:grid; grid-template-columns:repeat(4,minmax(0,1fr));
  gap:12px; margin:22px 0;
}
.card {
  background:var(--panel); border:1px solid var(--line);
  border-radius:14px; padding:17px; min-width:0;
}
.metric { font-size:29px; font-weight:bold; margin-top:8px; }
.layout {
  display:grid; grid-template-columns:repeat(2,minmax(0,1fr));
  gap:14px;
}
.actions { display:flex; flex-wrap:wrap; gap:8px; margin-top:12px; }
.actions button { flex:1; }
table { width:100%; border-collapse:collapse; font-size:13px; }
th,td {
  padding:11px 7px; text-align:left;
  border-bottom:1px solid var(--line);
}
th { color:var(--muted); }
.table-wrap { overflow-x:auto; }
.status {
  display:inline-block; padding:5px 8px; border-radius:20px;
  background:#25364a; font-size:11px;
}
.good { color:var(--teal); }
.wait { color:var(--amber); }
#message {
  margin-top:12px; padding:12px; border-radius:9px;
  background:#091629; color:var(--muted); overflow-wrap:anywhere;
}
footer {
  text-align:center; padding:25px 12px; color:var(--muted);
  font-size:12px;
}
@media(max-width:700px) {
  .stats { grid-template-columns:repeat(2,minmax(0,1fr)); }
  .layout { grid-template-columns:1fr; }
}
</style>
</head>
<body>
<header>
  <div>
    <h1>QuoteFlow AI</h1>
    <p>Digital Insurance Quotation Workspace</p>
  </div>
  <span class="tag">● PROTOTYPE MODE</span>
</header>

<main>
  <p class="tag">INSURANCE WORKFLOW AUTOMATION</p>
  <h2>Smarter quotations.<br>Less manual work.</h2>
  <p class="muted">
    A prototype for SME insurance submissions, data validation,
    quotation tracking, and underwriting review.
  </p>

  <section class="stats">
    <div class="card">
      <div class="muted">Open cases</div>
      <div class="metric" id="open">24</div>
    </div>
    <div class="card">
      <div class="muted">Validated</div>
      <div class="metric" id="validated">8</div>
    </div>
    <div class="card">
      <div class="muted">Under review</div>
      <div class="metric" id="review">4</div>
    </div>
    <div class="card">
      <div class="muted">Exceptions</div>
      <div class="metric" id="exceptions">3</div>
    </div>
  </section>

  <section class="layout">
    <div class="card">
      <h3>1. Upload census CSV</h3>
      <p class="muted">
        Upload a CSV containing company, employee_id, age, and plan.
        Use fictional data only.
      </p>
      <input type="file" id="file" accept=".csv">
      <div class="actions">
        <button class="primary" onclick="validateFile()">
          Validate file
        </button>
        <button class="secondary" onclick="sampleFile()">
          Load sample
        </button>
      </div>
      <div id="message" aria-live="polite">
        Waiting for a file.
      </div>
    </div>

    <div class="card">
      <h3>2. Quotation workflow</h3>
      <label for="company" class="muted">Customer / SME name</label>
      <input id="company" value="Northstar Trading"
        placeholder="Enter company name">
      <label for="caseId" class="muted">Quotation reference</label>
      <input id="caseId" value="QF-1042">
      <label for="stage" class="muted">Workflow status</label>
      <select id="stage">
        <option>New submission</option>
        <option>Validated</option>
        <option>Underwriting review</option>
        <option>Quotation prepared</option>
        <option>Exception flagged</option>
      </select>
      <div class="actions">
        <button class="primary" onclick="saveCase()">Save case</button>
        <button class="secondary" onclick="nextStage()">Advance status</button>
      </div>
      <p class="muted">
        Status changes are stored in this browser session only.
      </p>
    </div>

    <div class="card">
      <h3>3. Quotation pipeline</h3>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Reference</th><th>Customer</th><th>Status</th></tr>
          </thead>
          <tbody id="cases">
            <tr>
              <td>QF-1042</td><td>Northstar Trading</td>
              <td class="wait">New submission</td>
            </tr>
            <tr>
              <td>QF-1043</td><td>Cedar Works</td>
              <td class="good">Validated</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="actions">
        <button class="secondary" onclick="exportReport()">
          Export CSV report
        </button>
      </div>
    </div>

    <div class="card">
      <h3>4. Integration roadmap</h3>
      <p><span class="tag">01</span> Secure API connection to Salesforce</p>
      <p><span class="tag">02</span> Existing insurance rating engine</p>
      <p><span class="tag">03</span> Policy administration integration</p>
      <p><span class="tag">04</span> Arabic and English customer journey</p>
      <p><span class="tag">05</span> Access controls, audit logs and UAE compliance</p>
      <p class="muted">
        These are proposed future integrations, not currently connected.
      </p>
    </div>
  </section>
</main>

<footer>
  Concept demonstration only. Not affiliated with or endorsed by Cigna.
  No real insurance quotations or policies are issued.
  Do not upload real customer or medical information.
</footer>

<script>
const records = [
  {id:"QF-1042", company:"Northstar Trading", status:"New submission"},
  {id:"QF-1043", company:"Cedar Works", status:"Validated"}
];

const el = id => document.getElementById(id);

function message(text) {
  el("message").textContent = text;
}

function sampleFile() {
  const csv = [
    "company,employee_id,age,plan",
    "Northstar Trading,EMP001,34,Standard",
    "Northstar Trading,EMP002,41,Enhanced",
    "Northstar Trading,EMP003,29,Standard"
  ].join("\n");

  checkCSV(csv);
}

function validateFile() {
  const file = el("file").files[0];
  if (!file) {
    message("Choose a CSV file first.");
    return;
  }

  if (file.size > 2 * 1024 * 1024) {
    message("File is too large. Please use a CSV under 2 MB.");
    return;
  }

  const reader = new FileReader();
  reader.onload = () => checkCSV(String(reader.result));
  reader.onerror = () => message("Could not read this file.");
  reader.readAsText(file);
}

function checkCSV(csv) {
  const lines = csv.trim().split(/\r?\n/);
  if (lines.length < 2) {
    message("Add a header and at least one data row.");
    return;
  }

  // Simple CSV parser for this prototype; quoted commas
  // and multiline fields require a full CSV parsing library.
  const headers = lines[0].split(",").map(x =>
    x.trim().toLowerCase()
  );
  const required = ["company", "employee_id", "age", "plan"];
  const missing = required.filter(x => !headers.includes(x));

  if (missing.length) {
    message("Missing required columns: " + missing.join(", "));
    return;
  }

  const idx = Object.fromEntries(
    required.map(x => [x, headers.indexOf(x)])
  );
  const issues = [];

  lines.slice(1).forEach((line, i) => {
    const values = line.split(",").map(x => x.trim());
    required.forEach(key => {
      if (!values[idx[key]]) {
        issues.push("Row " + (i + 2) + ": " + key + " is blank.");
      }
    });

    const ageText = values[idx.age];
    const age = Number(ageText);
    if (ageText && (!Number.isFinite(age) || age < 0 || age > 120)) {
      issues.push("Row " + (i + 2) + ": age is invalid.");
    }
  });

  message(
    "Checked " + (lines.length - 1) + " data row(s). " +
    (issues.length
      ? issues.slice(0, 8).join(" ")
      : "Required fields passed basic checks. This is not underwriting approval.")
  );
}

function saveCase() {
  const id = el("caseId").value.trim();
  const company = el("company").value.trim();
  const status = el("stage").value;

  if (!id || !company) {
    message("Enter both a quotation reference and company name.");
    return;
  }

  const existing = records.find(r => r.id === id);
  if (existing) {
    existing.company = company;
    existing.status = status;
  } else {
    records.push({id, company, status});
    el("open").textContent = Number(el("open").textContent) + 1;
  }

  renderCases();
  message("Demo case saved locally: " + id);
}

function nextStage() {
  const options = Array.from(el("stage").options).map(o => o.value);
  const current = el("stage").value;
  const index = options.indexOf(current);
  el("stage").value = options[(index + 1) % options.length];
  saveCase();
}

function renderCases() {
  const tbody = el("cases");
  tbody.replaceChildren();

  records.forEach(r => {
    const tr = document.createElement("tr");
    [r.id, r.company, r.status].forEach((value, i) => {
      const td = document.createElement("td");
      td.textContent = value;
      if (i === 2) {
        td.className = value === "Validated" ||
          value === "Quotation prepared" ? "good" : "wait";
      }
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
}

function exportReport() {
  const escapeCSV = value =>
    '"' + String(value).replace(/"/g, '""') + '"';

  const csv = [
    ["reference", "company", "status"],
    ...records.map(r => [r.id, r.company, r.status])
  ].map(row => row.map(escapeCSV).join(",")).join("\n");

  const blob = new Blob([csv], {type:"text/csv;charset=utf-8"});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "quoteflow-demo-report.csv";
  a.click();
  URL.revokeObjectURL(url);
}

renderCases();
</script>
</body>
</html>

    
