import os
import base64

dir_path = r"c:\Users\adity\Desktop\Subjects\CLOUD\Assignment - 6"
html_path = os.path.join(dir_path, "assignment_6.html")
index_path = os.path.join(dir_path, "index.html")
images_dir = os.path.join(dir_path, "images")

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        print(f"Warning: image not found {image_path}")
        return ""
    ext = os.path.splitext(image_path)[1].lower().replace(".", "")
    if ext in ("jfif", "jpg", "jpeg"):
        mime = "image/jpeg"
    elif ext == "png":
        mime = "image/png"
    elif ext == "svg":
        mime = "image/svg+xml"
    else:
        mime = "image/png"
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{data}"

logo_b64 = get_base64_image(os.path.join(dir_path, "pccoelogo.jfif"))
step1_b64 = get_base64_image(os.path.join(images_dir, "step1_users_created.png"))
step2_b64 = get_base64_image(os.path.join(images_dir, "step2_admin_group.png"))
step3_b64 = get_base64_image(os.path.join(images_dir, "step3_readonly_user.png"))
step4_b64 = get_base64_image(os.path.join(images_dir, "step4_custom_policy.png"))
step5_b64 = get_base64_image(os.path.join(images_dir, "step5_admin_test_allow.png"))
step6_b64 = get_base64_image(os.path.join(images_dir, "step6_readonly_test_deny.png"))
step7_b64 = get_base64_image(os.path.join(images_dir, "step7_readonly_test_allow.png"))
step8_b64 = get_base64_image(os.path.join(images_dir, "step8_custom_policy_test_deny.png"))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloud Computing Lab 6 - Cloud Security Basics (IAM & Permissions)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 10.5pt;
    line-height: 1.78;
    word-spacing: 0.08em;
    letter-spacing: 0.015em;
    color: #1e293b;
    background: #e2e8f0;
    padding: 36px 16px;
    -webkit-font-smoothing: antialiased;
  }}

  .container {{
    max-width: 8.5in;
    margin: 0 auto;
  }}

  .page {{
    min-height: 11in;
    width: 8.5in;
    padding: 0.75in 0.85in;
    background: #ffffff;
    margin: 0 auto 36px auto;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.08), 0 8px 12px -6px rgba(0, 0, 0, 0.04);
    position: relative;
    box-sizing: border-box;
    border-radius: 4px;
  }}

  .page:focus-within {{
    outline: 2px dashed #0284c7;
  }}

  @page {{
    size: letter;
    margin: 0.4in 0.5in;
  }}

  @media print {{
    html, body {{
      background: #ffffff !important;
      padding: 0 !important;
      margin: 0 !important;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    .container {{
      max-width: 100% !important;
      width: 100% !important;
      margin: 0 !important;
      box-shadow: none !important;
      padding: 0 !important;
    }}
    .page {{
      width: 100% !important;
      min-height: auto !important;
      height: auto !important;
      max-height: none !important;
      overflow: visible !important;
      margin: 0 !important;
      padding: 0 !important;
      box-shadow: none !important;
      border: none !important;
      page-break-after: always !important;
      break-after: page !important;
      page-break-inside: avoid !important;
      break-inside: avoid !important;
      border-radius: 0 !important;
      box-sizing: border-box !important;
    }}
    .page:last-child {{
      page-break-after: avoid !important;
      break-after: avoid !important;
    }}
    table, pre, .info-box, .free-img {{
      page-break-inside: avoid !important;
      break-inside: avoid !important;
    }}
  }}

  /* PCCOE Cover Header Table */
  .cover-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 24px;
    font-family: 'Times New Roman', Times, serif;
  }}
  .cover-table td {{
    border: 1px solid #000;
    padding: 8px 14px;
  }}
  .cover-table .college-info {{
    text-align: center;
    font-weight: bold;
    font-size: 15.5pt;
    line-height: 1.4;
    letter-spacing: 0.02em;
  }}
  .cover-table .row-centered {{
    text-align: center;
    font-weight: bold;
    font-size: 13.8pt;
    padding: 8px 14px;
  }}
  .cover-table .row-left {{
    text-align: left;
    font-weight: bold;
    font-size: 12.8pt;
    padding: 7px 14px;
  }}
  .logo-container {{
    text-align: center;
    width: 18%;
    padding: 6px !important;
  }}
  .logo-container img {{
    max-width: 95px;
    height: auto;
    display: block;
    margin: 0 auto;
  }}

  /* Typography */
  h2 {{
    font-size: 13.8pt;
    font-weight: 800;
    color: #0f172a;
    margin-top: 26px;
    margin-bottom: 14px;
    border-bottom: 2.5px solid #0284c7;
    padding-bottom: 6px;
    letter-spacing: 0.02em;
    text-transform: uppercase;
  }}
  h3 {{
    font-size: 11.8pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 22px;
    margin-bottom: 12px;
    line-height: 1.5;
    letter-spacing: 0.015em;
  }}
  h4 {{
    font-size: 10.6pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 16px;
    margin-bottom: 8px;
    line-height: 1.5;
  }}
  p {{
    text-align: justify;
    line-height: 1.78;
    margin-bottom: 16px;
    color: #334155;
    word-spacing: 0.08em;
  }}
  ol, ul {{
    margin-left: 28px;
    margin-bottom: 18px;
    color: #334155;
  }}
  li {{
    margin-bottom: 10px;
    line-height: 1.72;
    word-spacing: 0.07em;
  }}

  code {{
    font-family: 'Fira Code', monospace;
    font-size: 9pt;
    background: #f1f5f9;
    color: #0369a1;
    padding: 2px 6px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
    letter-spacing: 0;
  }}

  pre {{
    background: #0f172a;
    color: #f8fafc;
    border: 1px solid #334155;
    border-radius: 7px;
    padding: 14px 18px;
    font-family: 'Fira Code', monospace;
    font-size: 8.8pt;
    line-height: 1.58;
    margin: 14px 0 18px 0;
    overflow-x: auto;
  }}
  pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
  }}

  /* Styled Tables */
  .styled-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 16px 0 20px 0;
    font-size: 9.3pt;
    background: #ffffff;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #cbd5e1;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
  }}
  .styled-table thead th {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 8.3pt;
    letter-spacing: 0.06em;
    padding: 10px 14px;
    border: none;
    text-align: left;
  }}
  .styled-table tbody td {{
    padding: 10px 14px;
    border-bottom: 1px solid #e2e8f0;
    border-right: 1px solid #f1f5f9;
    color: #1e293b;
    vertical-align: top;
    line-height: 1.6;
    word-spacing: 0.05em;
  }}
  .styled-table tbody tr:last-child td {{
    border-bottom: none;
  }}
  .styled-table tbody tr:nth-child(even) {{
    background-color: #f8fafc;
  }}

  /* Info Callouts */
  .info-box {{
    border-radius: 8px;
    padding: 13px 18px;
    margin: 18px 0;
    font-size: 9.7pt;
    line-height: 1.68;
    border-left: 4.5px solid;
    word-spacing: 0.06em;
  }}
  .info-box.blue {{
    background: #f0f9ff;
    border-color: #0284c7;
    color: #0c4a6e;
  }}
  .info-box.green {{
    background: #f0fdf4;
    border-color: #16a34a;
    color: #14532d;
  }}
  .info-box.amber {{
    background: #fffbeb;
    border-color: #d97706;
    color: #78350f;
  }}
  .info-box.purple {{
    background: #faf5ff;
    border-color: #9333ea;
    color: #581c87;
  }}

  /* Free Pasted Images - Big, natural, zero borders, zero boxes */
  .free-img {{
    margin: 22px 0 10px 0;
    text-align: center;
    background: transparent;
    border: none;
    padding: 0;
  }}
  .free-img img {{
    width: 100%;
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
    border: none;
    outline: none;
    box-shadow: none;
    border-radius: 0;
    background: transparent;
  }}
  .caption {{
    font-size: 9pt;
    color: #475569;
    text-align: center;
    margin-top: 9px;
    margin-bottom: 22px;
    font-style: italic;
    line-height: 1.5;
  }}

  .badge {{
    display: inline-block;
    padding: 3px 8px;
    border-radius: 5px;
    font-size: 7.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}
  .badge-aws {{
    background: #ffedd5;
    color: #c2410c;
    border: 1px solid #fdba74;
  }}
  .badge-success {{
    background: #dcfce7;
    color: #15803d;
    border: 1px solid #86efac;
  }}
  .badge-danger {{
    background: #fee2e2;
    color: #b91c1c;
    border: 1px solid #fca5a5;
  }}
</style>
</head>
<body>
<div class="container" contenteditable="true">

  <!-- ==========================================================================
       PAGE 1: COVER TABLE, TITLE, AIM & OBJECTIVES
       ========================================================================== -->
  <div class="page">
    <table class="cover-table">
      <tr>
        <td class="logo-container">
          <img src="{logo_b64}" alt="PCCOE Logo" contenteditable="false">
        </td>
        <td class="college-info">
          Pimpri Chinchwad Education Trust's<br>
          Pimpri Chinchwad College of Engineering
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-centered">
          Assignment / Laboratory Practical No. 6
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left">
          Course:- Cloud Computing (Laboratory)
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left">
          Name:- Aditya Chandrajit Deore
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left">
          PRN:- 124B1F116 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Batch:- B3
        </td>
      </tr>
    </table>

    <h2>Title</h2>
    <p style="font-size: 11pt; margin-bottom: 8px;">
      <strong>Lab 6:</strong> Cloud Security Basics (Identity &amp; Access Management - IAM &amp; Permissions)
    </p>
    <p style="margin-bottom: 20px;">
      <span class="badge badge-aws">Cloud Platform: Amazon Web Services (AWS)</span> &bull; 
      <strong>Service:</strong> Identity &amp; Access Management (IAM) &bull; 
      <strong>Scope:</strong> Global (Zero Regional Lock-in, 100% Free Service Tier)
    </p>

    <h2>Aim</h2>
    <p>
      To understand, configure, and evaluate cloud security governance mechanisms using Identity and Access Management (IAM), including multi-tenant digital identity creation, group-based access administration, granular JSON policy formulation adhering to the Principle of Least Privilege (PoLP), policy simulation verification across Administrator, Read-Only, and Custom roles, and Multi-Factor Authentication (MFA) enforcement.
    </p>

    <h2 style="margin-top: 14px; margin-bottom: 6px;">Objectives</h2>
    <ol style="margin-bottom: 8px;">
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To define the architectural role of Identity and Access Management (IAM) as the centralized authentication and authorization control plane in modern cloud computing.</li>
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To analyze the critical security justifications for IAM, focusing on eliminating shared root credentials, maintaining non-repudiable audit trails, and shrinking attack blast radiuses.</li>
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To delineate the architectural differences, credential lifecycles, and delegation mechanics between IAM Users, Groups, and Roles.</li>
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To deconstruct JSON policy grammar (<code>Effect</code>, <code>Action</code>, <code>Resource</code>, <code>Condition</code>) and master deterministic policy evaluation rules (Explicit Deny vs. Explicit Allow vs. Default Deny).</li>
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To implement the Principle of Least Privilege (PoLP) by designing customized, laser-scoped policies restricting cloud actions to strictly required operational subsets.</li>
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To investigate Multi-Factor Authentication (MFA) paradigms (TOTP, FIDO2/WebAuthn) and evaluate policy-driven conditional access mechanisms.</li>
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To compare the security posture, operational velocity, and governance overhead of Administrator, Read-Only, and Custom role tiers.</li>
      <li style="margin-bottom: 4px; line-height: 1.5; font-size: 9.3pt;">To provision IAM users (<code>lab6-admin</code>, <code>lab6-viewer</code>, <code>lab6-operator</code>), assign managed and custom policies, and empirically validate access boundaries using the AWS IAM Policy Simulator.</li>
    </ol>
  </div>

  <!-- ==========================================================================
       PAGE 2: PART A - Q1: WHAT IS IAM IN CLOUD COMPUTING?
       ========================================================================== -->
  <div class="page">
    <h2>Part A &mdash; Theoretical Foundations</h2>

    <h3>1. What is IAM (Identity &amp; Access Management) in Cloud Computing?</h3>
    <p>
      <strong>Identity and Access Management (IAM)</strong> is the foundational security framework and centralized management plane in cloud computing that securely controls <em>WHO</em> (authenticated entities: human operators, background software daemons, containerized microservices, or external federated systems) can perform <em>WHAT</em> actions on <em>WHICH</em> specific cloud resources, under <em>WHICH</em> operational conditions.
    </p>

    <p>
      In modern hyperscale cloud platforms, computing infrastructure is completely software-defined and driven by network APIs. Consequently, traditional physical access restrictions are replaced by identity-based guardrails. IAM architecture is bifurcated into two indispensable, sequential security checkpoints:
    </p>

    <ul>
      <li>
        <strong>Authentication (AuthN) &mdash; "Who are you?":</strong><br>
        The initial process of positively validating the claimed digital identity of an incoming entity before admitting it into the cloud control plane. Authentication credentials include:
        <ul style="margin-top: 6px; margin-bottom: 6px;">
          <li>Console passwords for graphical user interface (GUI) access.</li>
          <li>Cryptographic programmatic API access keys (<code>Access Key ID</code> and <code>Secret Access Key</code>) for Command Line Interface (CLI) and Software Development Kit (SDK) access.</li>
          <li>Temporary session tokens dynamically minted by the AWS Security Token Service (STS).</li>
          <li>Multi-Factor Authentication (MFA) time-based codes or cryptographic security tokens.</li>
          <li>Federated identity assertions using SAML 2.0 or OpenID Connect (OIDC).</li>
        </ul>
      </li>
      <li>
        <strong>Authorization (AuthZ) &mdash; "What are you permitted to do?":</strong><br>
        The subsequent process of determining the exact API actions the authenticated identity is granted permission to execute against target cloud resources. Authorization is evaluated dynamically at runtime by policy evaluation engines inspecting attached declarative JSON policies.
      </li>
    </ul>

    <div class="info-box blue">
      <strong>Architectural Context:</strong> In AWS, IAM is a <em>global service</em> requiring no regional endpoint selection. Every single incoming API request across all cloud services (EC2, S3, RDS, Lambda, VPC) is intercepted at the edge and evaluated against IAM authorization policies before execution is allowed. IAM carries no operational usage fees.
    </div>

    <div class="info-box green">
      <strong>Key Takeaway:</strong> Authentication verifies identity; Authorization verifies permissions. An identity must successfully pass both checks before any cloud resource can be accessed or modified.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 3: Q2: WHY IS IAM IMPORTANT FOR SECURING CLOUD RESOURCES?
       ========================================================================== -->
  <div class="page">
    <h3>2. Why is IAM Important for Securing Cloud Resources?</h3>
    <p>
      In cloud computing, traditional physical perimeter defenses (such as firewalls and DMZ boundaries) are insufficient because cloud resources are software-defined and remotely accessible via public RESTful APIs. Consequently, <strong>Identity is the new security perimeter</strong>. IAM is crucial for cloud security due to the following pillars:
    </p>

    <ul>
      <li>
        <strong>Elimination of Shared Root Credentials:</strong><br>
        The account root user possesses unrestricted, god-mode administrative power. IAM enables administrators to lock away the root account and provision unique, personal identities for every engineer and workload. Access can be granted, audited, or revoked individually without impacting others.
      </li>
      <li>
        <strong>Enforcement of Least Privilege (Blast Radius Containment):</strong><br>
        By constraining users and microservices strictly to the operations required for their specific job functions, the damage resulting from human error or compromised credentials is tightly bounded.
      </li>
      <li>
        <strong>Comprehensive Non-Repudiable Auditability:</strong><br>
        Every API call &mdash; whether executed via the AWS Management Console, CLI, SDK, or Terraform &mdash; is intercepted and stamped with the caller's unique IAM ARN, timestamp, source IP, and parameters into immutable audit trails (such as AWS CloudTrail), enabling rapid forensic analysis and regulatory compliance (SOC 2, ISO 27001, PCI-DSS).
      </li>
      <li>
        <strong>Dynamic Ephemeral Credentialing via Roles:</strong><br>
        Eliminates dangerous hardcoded, long-term API keys in codebases by providing short-lived, auto-rotating STS credentials for compute workloads (EC2 instances, ECS containers, Lambda functions).
      </li>
      <li>
        <strong>Multi-Factor Authentication (MFA) Enforcement:</strong><br>
        Adds an essential physical possession barrier, neutralizing credential stuffing, password reuse, and phishing compromises across both console and programmatic access points.
      </li>
    </ul>

    <div class="info-box amber">
      <strong>Security Impact:</strong> Without IAM, anyone possessing the root account credentials would hold unlimited authority to destroy infrastructure, expose customer records, or incur catastrophic billing costs. IAM turns a raw cloud account into a securely governable, multi-tenant enterprise environment.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 4: Q3: DIFFERENCE BETWEEN USERS, GROUPS, AND ROLES
       ========================================================================== -->
  <div class="page">
    <h3>3. Difference Between Users, Groups, and Roles in IAM</h3>
    <p>
      IAM organizes access governance across three distinct identity primitives, each tailored to specific operational lifecycles and trust models:
    </p>

    <table class="styled-table">
      <thead>
        <tr>
          <th style="width: 17%;">Entity Type</th>
          <th style="width: 25%;">Core Definition</th>
          <th style="width: 20%;">Credential Structure</th>
          <th style="width: 18%;">Session Lifespan</th>
          <th style="width: 20%;">Primary Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>IAM User</strong></td>
          <td>A unique digital identity created within an AWS account representing a specific individual person or legacy application needing long-term access.</td>
          <td><strong>Long-term:</strong> Console password (interactive GUI) and/or Access Key ID + Secret Access Key (programmatic CLI/SDK).</td>
          <td>Persistent until explicitly rotated, deactivated, or deleted by an administrator.</td>
          <td>Individual system administrators, software developers, or on-premises servers syncing data.</td>
        </tr>
        <tr>
          <td><strong>IAM Group<br>(User Group)</strong></td>
          <td>A logical collection of IAM users who share common operational functions. Cannot be identified as a principal in policies and cannot log in.</td>
          <td><strong>None:</strong> Groups possess no passwords, access keys, or certificates. Members inherit group permissions.</td>
          <td>N/A (Administrative grouping mechanism; no interactive session exists).</td>
          <td>Managing permissions at scale (e.g., <code>Developers</code>, <code>DevOps</code>, <code>Auditors</code>, <code>DBAs</code>) without editing individual users.</td>
        </tr>
        <tr>
          <td><strong>IAM Role</strong></td>
          <td>An identity with defined permissions that is NOT tied to a specific person or long-term credential; assumed temporarily by trusted entities.</td>
          <td><strong>Temporary &amp; Ephemeral:</strong> AWS STS issues short-lived Access Key, Secret Key, and Session Token.</td>
          <td>Short-lived (Configurable from 15 minutes up to 12 hours; auto-expires).</td>
          <td>Compute workloads (EC2, Lambda), cross-account delegation, and federated SSO (Okta, Azure AD).</td>
        </tr>
      </tbody>
    </table>

    <div class="info-box green">
      <strong>Key Architectural Distinction:</strong> An IAM User has long-term static credentials. An IAM Group is merely an administrative container to attach policies to multiple users at once. An IAM Role has no static credentials; it is dynamically assumed by trusted actors who receive short-lived temporary tokens via AWS STS.
    </div>

    <div class="info-box blue">
      <strong>Best Practice Note:</strong> Avoid attaching policies directly to individual IAM users. Instead, place users inside IAM Groups and attach policies to those groups, ensuring clean role-based access control (RBAC).
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 5: Q4: PERMISSIONS & POLICIES (HOW THEY CONTROL ACCESS)
       ========================================================================== -->
  <div class="page">
    <h3>4. What are Permissions and Policies, and How Do They Control Access?</h3>
    <p>
      <strong>Permissions</strong> are granular, atomic authorizations that dictate whether a specific action on a specific cloud resource is granted or prohibited (e.g., allowing <code>ec2:StartInstances</code> on an EC2 server or <code>s3:GetObject</code> on a storage bucket). In cloud architectures, permissions are never assigned arbitrarily; they are formally structured into declarative JSON documents termed <strong>Policies</strong>.
    </p>

    <h4>Anatomy of an IAM Policy Document:</h4>
    <pre style="margin: 6px 0; padding: 6px 12px; font-size: 8pt; line-height: 1.35;"><code>{{
  "Version": "2012-10-17",
  "Statement": [
    {{
      "Sid": "AllowEC2StartStopReadOnly",
      "Effect": "Allow",
      "Action": ["ec2:Describe*", "ec2:StartInstances", "ec2:StopInstances"],
      "Resource": "*",
      "Condition": {{ "Bool": {{ "aws:MultiFactorAuthPresent": "true" }} }}
    }}
  ]
}}</code></pre>

    <ul style="margin-bottom: 8px;">
      <li style="margin-bottom: 3px; line-height: 1.5; font-size: 9.3pt;"><strong>Effect:</strong> Must be explicitly set to either <code>"Allow"</code> or <code>"Deny"</code>.</li>
      <li style="margin-bottom: 3px; line-height: 1.5; font-size: 9.3pt;"><strong>Action:</strong> The specific API method calls governed by the statement (e.g., <code>ec2:RunInstances</code>).</li>
      <li style="margin-bottom: 3px; line-height: 1.5; font-size: 9.3pt;"><strong>Resource:</strong> The target Amazon Resource Name (ARN) upon which actions are permitted or denied.</li>
      <li style="margin-bottom: 3px; line-height: 1.5; font-size: 9.3pt;"><strong>Condition (Optional):</strong> Granular context keys restricting execution (e.g., requiring MFA).</li>
    </ul>

    <h4>The IAM Policy Evaluation Logic:</h4>
    <p style="margin-bottom: 6px;">When an incoming API request reaches AWS, the IAM Policy Engine processes policies using strict deterministic rules:</p>
    <ol style="margin-bottom: 8px;">
      <li style="margin-bottom: 3px; line-height: 1.5; font-size: 9.3pt;"><strong>Default Deny:</strong> By default, all requests are implicitly denied.</li>
      <li style="margin-bottom: 3px; line-height: 1.5; font-size: 9.3pt;"><strong>Explicit Deny Overrides Everything:</strong> If any policy statement evaluates to <code>Deny</code>, the request is immediately rejected.</li>
      <li style="margin-bottom: 3px; line-height: 1.5; font-size: 9.3pt;"><strong>Explicit Allow Required:</strong> In the absence of an explicit Deny, the request must have at least one explicit <code>Allow</code> statement.</li>
    </ol>
  </div>

  <!-- ==========================================================================
       PAGE 6: Q5: LEAST PRIVILEGE PRINCIPLE & Q6: MFA
       ========================================================================== -->
  <div class="page">
    <h3>5. What is the Least Privilege Principle? Why is it Important in Cloud Security?</h3>
    <p>
      The <strong>Principle of Least Privilege (PoLP)</strong> is a cardinal cybersecurity doctrine dictating that every identity (human user, background process, compute instance, or automation script) must be granted strictly the <em>bare minimum permissions</em> necessary to accomplish its intended operational function &mdash; and absolutely nothing more.
    </p>

    <ul>
      <li>
        <strong>Drastic Blast Radius Mitigation:</strong><br>
        In cloud environments, credential exposure is a primary attack vector. If a developer's API key is accidentally committed to a public repository, an identity adhering to least privilege (e.g., read-only access to a specific dev bucket) prevents the adversary from destroying databases, altering route tables, or spinning up expensive cryptocurrency miners.
      </li>
      <li>
        <strong>Protection Against Human Error:</strong><br>
        Prevents engineers from inadvertently terminating mission-critical production clusters or dropping primary storage volumes during routine maintenance.
      </li>
      <li>
        <strong>Regulatory Compliance:</strong><br>
        Mandated by leading governance standards including PCI-DSS (Req 7), ISO/IEC 27001 (Control A.9.2), SOC 2 Trust Services, and CIS AWS Foundations Benchmarks.
      </li>
    </ul>

    <h3>6. What is MFA (Multi-Factor Authentication) and How Does it Enhance Account Security?</h3>
    <p>
      <strong>Multi-Factor Authentication (MFA)</strong> is a critical identity verification defense requiring a user to furnish two or more distinct, independent categories of authentication factors before access to cloud consoles or APIs is authorized. In computer security, factors are categorized into:
    </p>
    <ul>
      <li><strong>Knowledge Factor (Something You Know):</strong> Static passwords, passphrases, or security PINs.</li>
      <li><strong>Possession Factor (Something You Have):</strong> A physical smartphone generating Time-based One-Time Passwords (TOTP via Google Authenticator, Microsoft Authenticator), a hardware cryptographic token (YubiKey / FIDO2 security key), or an SMS/email verification token.</li>
      <li><strong>Inherence Factor (Something You Are):</strong> Biometric identifiers (fingerprints, retina patterns, facial geometry).</li>
    </ul>

    <h4>How MFA Enhances Cloud Account Security:</h4>
    <ul>
      <li><strong>Neutralizes Credential Theft &amp; Phishing:</strong> Over 99% of bulk automated credential stuffing, brute-force dictionary attacks, and phishing compromises are neutralized by MFA. Even if an adversary captures a user's password, authentication fails without the live, rotating TOTP code generated on the victim's physical device.</li>
      <li><strong>Protection of Privileged &amp; Root Accounts:</strong> Requiring MFA for all administrative sessions is the single highest-impact security control in cloud governance.</li>
      <li><strong>Policy-Enforced Conditional Access:</strong> Mandates an active MFA session (<code>"aws:MultiFactorAuthPresent": "true"</code>) before allowing destructive actions like terminating servers or deleting storage volumes.</li>
    </ul>
  </div>

  <!-- ==========================================================================
       PAGE 7: Q7: ADMIN VS READ-ONLY VS CUSTOM ROLES
       ========================================================================== -->
  <div class="page">
    <h3>7. What are the Differences Between Admin, Read-Only, and Custom Roles in IAM?</h3>
    <p>
      Cloud governance categorizes access into distinct permission tiers depending on operational responsibility and trust boundaries:
    </p>

    <table class="styled-table">
      <thead>
        <tr>
          <th style="width: 18%;">Permission Tier</th>
          <th style="width: 25%;">Scope of Access</th>
          <th style="width: 19%;">Risk &amp; Blast Radius</th>
          <th style="width: 20%;">Maintenance Effort</th>
          <th style="width: 18%;">Typical Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Administrator Role<br>(<code>AdministratorAccess</code>)</strong></td>
          <td>Unrestricted superuser access to all AWS services and API actions (<code>Action: "*", Resource: "*"</code>). Can manage billing, users, encryption, and networks.</td>
          <td><strong>Extreme:</strong> Compromise results in complete account takeover, data destruction, or multi-thousand dollar rogue resource bills.</td>
          <td><strong>Zero maintenance:</strong> Pre-built, maintained, and automatically updated by the cloud provider.</td>
          <td>Initial cloud account bootstrapping, emergency break-glass procedures, senior infrastructure leads only.</td>
        </tr>
        <tr>
          <td><strong>Read-Only Role<br>(<code>ReadOnlyAccess</code>)</strong></td>
          <td>Permits viewing, listing, and describing resources across all services (<code>Get*</code>, <code>Describe*</code>, <code>List*</code>). Strictly blocks all write, create, update, and delete actions.</td>
          <td><strong>Low to Moderate:</strong> Zero risk of data loss or service disruption. Data confidentiality risk remains if sensitive resources are visible.</td>
          <td><strong>Zero maintenance:</strong> Pre-built AWS managed policy covering all existing and newly released services automatically.</td>
          <td>Security auditors, third-party compliance assessors, junior interns, and external monitoring dashboards.</td>
        </tr>
        <tr>
          <td><strong>Custom Role / Policy<br>(e.g., <code>lab6-ec2-operator</code>)</strong></td>
          <td>Laser-focused, bespoke JSON policies specifying exact API verbs (e.g., <code>ec2:StartInstances</code>) on designated resource ARNs only.</td>
          <td><strong>Minimal:</strong> Strict adherence to Least Privilege. Attack blast radius is confined strictly to the whitelisted actions.</td>
          <td><strong>Moderate to High:</strong> Must be manually authored, tested, documented, and updated as application requirements evolve.</td>
          <td>Production workloads, automated CI/CD deployment pipelines, day-to-day engineers performing scoped duties.</td>
        </tr>
      </tbody>
    </table>

    <div class="info-box purple">
      <strong>Governance Recommendation:</strong> In enterprise production environments, granting direct administrative access should be strictly limited to break-glass accounts. Over 90% of team members should operate under carefully designed Custom policies tailored to their operational domain.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 8: PART B - STEP 1 (CREATE THREE IAM USERS)
       ========================================================================== -->
  <div class="page">
    <h2>Part B &mdash; Practical: IAM Users, Groups, Policies &amp; Simulator Testing</h2>
    <p>
      In this laboratory practical, an enterprise identity structure was implemented in AWS IAM. Three distinct users were provisioned, assigned varying permission tiers (Administrator, Read-Only, and Custom Least-Privilege), and systematically evaluated using the AWS IAM Policy Simulator to prove deterministic boundary enforcement.
    </p>

    <h3>Step 1 &mdash; Create Three IAM Users</h3>
    <p>
      Navigated to <strong>AWS IAM Console &rarr; Users &rarr; Create user</strong>. Provisioned three independent users representing different organizational roles:
    </p>
    <ol>
      <li><code>lab6-admin</code>: Designated for full infrastructure management and system administration.</li>
      <li><code>lab6-viewer</code>: Designated for auditing, resource discovery, and monitoring without modification rights.</li>
      <li><code>lab6-operator</code>: Designated for targeted compute operations (starting and stopping EC2 instances only).</li>
    </ol>
    <p>
      <em>Note:</em> In accordance with laboratory safety standards, no console passwords or long-term access keys were generated for these users, as permission boundaries were evaluated directly via the authoritative AWS IAM Policy Simulator engine.
    </p>

    <div class="free-img">
      <img src="{step1_b64}" alt="Step 1 - IAM Users Created">
    </div>
    <p class="caption">Figure 1: AWS IAM Users dashboard displaying all three newly provisioned users (<code>lab6-admin</code>, <code>lab6-operator</code>, and <code>lab6-viewer</code>).</p>
  </div>

  <!-- ==========================================================================
       PAGE 9: STEP 2 (CREATE ADMIN GROUP)
       ========================================================================== -->
  <div class="page">
    <h3>Step 2 &mdash; Create the <code>lab6-admins</code> User Group with <code>AdministratorAccess</code></h3>
    <p>
      To implement access control best practices (never attaching administrative privileges directly to individual users), an IAM User Group was created:
    </p>
    <ol>
      <li>Navigated to <strong>IAM &rarr; User groups &rarr; Create group</strong>.</li>
      <li>Configured User group name: <code>lab6-admins</code>.</li>
      <li>Attached the AWS-managed policy: <code>AdministratorAccess</code> (ARN: <code>arn:aws:iam::aws:policy/AdministratorAccess</code>).</li>
      <li>Added user <code>lab6-admin</code> as a member of the group.</li>
    </ol>
    <p>
      By leveraging group-based inheritance, <code>lab6-admin</code> inherits full administrative privileges without requiring inline or user-level policy clutter, establishing scalable identity governance.
    </p>

    <div class="free-img">
      <img src="{step2_b64}" alt="Step 2 - Admin Group Created">
    </div>
    <p class="caption">Figure 2: User group <code>lab6-admins</code> overview showing attached policy <code>AdministratorAccess</code> and assigned member <code>lab6-admin</code>.</p>
  </div>

  <!-- ==========================================================================
       PAGE 10: STEP 3 (READ-ONLY ACCESS FOR VIEWER)
       ========================================================================== -->
  <div class="page">
    <h3>Step 3 &mdash; Give <code>lab6-viewer</code> Read-Only Access</h3>
    <p>
      To configure an auditor profile with wide visibility but zero modification permissions:
    </p>
    <ol>
      <li>Navigated to <strong>IAM &rarr; Users &rarr; lab6-viewer &rarr; Permissions tab</strong>.</li>
      <li>Selected <strong>Add permissions &rarr; Attach policies directly</strong>.</li>
      <li>Searched for and selected the AWS-managed policy: <code>ReadOnlyAccess</code> (ARN: <code>arn:aws:iam::aws:policy/ReadOnlyAccess</code>).</li>
      <li>Reviewed and confirmed attachment.</li>
    </ol>
    <p>
      The <code>ReadOnlyAccess</code> policy allows the viewer to query metadata, inspect configurations, and list resources across all AWS services, but strictly denies all mutating API operations (such as <code>RunInstances</code>, <code>DeleteBucket</code>, or <code>CreateUser</code>).
    </p>

    <div class="free-img">
      <img src="{step3_b64}" alt="Step 3 - ReadOnlyAccess Attached to Viewer">
    </div>
    <p class="caption">Figure 3: User permissions tab for <code>lab6-viewer</code> confirming direct attachment of the AWS-managed <code>ReadOnlyAccess</code> policy.</p>
  </div>

  <!-- ==========================================================================
       PAGE 11: STEP 4 (CUSTOM LEAST-PRIVILEGE POLICY)
       ========================================================================== -->
  <div class="page">
    <h3>Step 4 &mdash; Create a Custom Least-Privilege Policy for <code>lab6-operator</code></h3>
    <p>
      To demonstrate the Principle of Least Privilege (PoLP), a bespoke customer-managed JSON policy was authored to restrict <code>lab6-operator</code> to only starting, stopping, and describing EC2 compute instances:
    </p>
    <ol style="margin-bottom: 8px;">
      <li style="margin-bottom: 3px; line-height: 1.45; font-size: 9.3pt;">Navigated to <strong>IAM &rarr; Policies &rarr; Create policy</strong>.</li>
      <li style="margin-bottom: 3px; line-height: 1.45; font-size: 9.3pt;">Switched to JSON editor and specified the custom policy:
        <pre style="margin: 4px 0; padding: 5px 10px; font-size: 7.8pt; line-height: 1.35;"><code>{{
  "Version": "2012-10-17",
  "Statement": [{{
    "Sid": "VisualEditor0", "Effect": "Allow",
    "Action": ["ec2:Describe*", "ec2:StartInstances", "ec2:StopInstances"], "Resource": "*"
  }}]
}}</code></pre>
      </li>
      <li style="margin-bottom: 3px; line-height: 1.45; font-size: 9.3pt;">Named the policy <code>lab6-ec2-operator</code> (allows EC2 describe, start, and stop only).</li>
      <li style="margin-bottom: 3px; line-height: 1.45; font-size: 9.3pt;">Attached this policy directly to user <code>lab6-operator</code>.</li>
    </ol>

    <div class="free-img">
      <img src="{step4_b64}" alt="Step 4 - Custom Policy Created" style="max-height: 310px;">
    </div>
    <p class="caption">Figure 4: Creation and summary of custom policy <code>lab6-ec2-operator</code> restricting actions strictly to EC2 Describe, Start, and Stop.</p>
  </div>

  <!-- ==========================================================================
       PAGE 12: STEP 5 (POLICY SIMULATOR - ADMIN ALLOW)
       ========================================================================== -->
  <div class="page">
    <h3>Step 5 &mdash; Test: Admin CAN Launch Instances (<code>ec2:RunInstances</code>)</h3>
    <p>
      To authoritatively verify authorization policies without requiring credential deployment or running live billable workloads, the <strong>AWS IAM Policy Simulator</strong> was utilized:
    </p>
    <ol>
      <li>Opened the <strong>AWS IAM Policy Simulator</strong> console.</li>
      <li>Selected User: <code>lab6-admin</code> from the Users pane.</li>
      <li>Selected Service: <strong>EC2</strong> and checked Action: <code>RunInstances</code>.</li>
      <li>Clicked <strong>Run Simulation</strong>.</li>
    </ol>
    <p>
      <strong>Evaluation Result:</strong> The simulator returned <span class="badge badge-success">Allowed</span> across all five associated resource types (instance, volume, network-interface, subnet, image) via <strong>Explicit allow</strong> stemming from the inherited <code>AdministratorAccess</code> policy. This confirms that administrative identities hold full provisioning authority.
    </p>

    <div class="free-img">
      <img src="{step5_b64}" alt="Step 5 - Admin Allowed to Launch Instances">
    </div>
    <p class="caption">Figure 5: IAM Policy Simulator testing <code>lab6-admin</code> executing <code>ec2:RunInstances</code> &mdash; Result: Allowed on all resources (Explicit allow).</p>
  </div>

  <!-- ==========================================================================
       PAGE 13: STEP 6 (POLICY SIMULATOR - VIEWER DENY)
       ========================================================================== -->
  <div class="page">
    <h3>Step 6 &mdash; Test: Read-Only User CANNOT Launch Instances (<code>ec2:RunInstances</code>)</h3>
    <p>
      Next, verified whether <code>lab6-viewer</code>'s <code>ReadOnlyAccess</code> successfully prevents modifying or launching compute infrastructure:
    </p>
    <ol>
      <li>Selected User: <code>lab6-viewer</code> in the IAM Policy Simulator.</li>
      <li>Selected Service: <strong>EC2</strong> and Action: <code>RunInstances</code>.</li>
      <li>Clicked <strong>Run Simulation</strong>.</li>
    </ol>
    <p>
      <strong>Evaluation Result:</strong> The simulator returned <span class="badge badge-danger">Denied</span> with permission state <strong>Implicit deny</strong>. Because <code>ReadOnlyAccess</code> only allows reading actions (<code>Describe*</code>, <code>Get*</code>, <code>List*</code>) and contains no <code>Allow</code> statement for instance creation, the default deny rule blocked the action completely.
    </p>

    <div class="free-img">
      <img src="{step6_b64}" alt="Step 6 - Viewer Denied Launching Instances">
    </div>
    <p class="caption">Figure 6: IAM Policy Simulator testing <code>lab6-viewer</code> executing <code>ec2:RunInstances</code> &mdash; Result: Denied (Implicit deny).</p>
  </div>

  <!-- ==========================================================================
       PAGE 14: STEP 7 (POLICY SIMULATOR - VIEWER ALLOW DESCRIBE)
       ========================================================================== -->
  <div class="page">
    <h3>Step 7 &mdash; Test: Read-Only User CAN Describe Instances (<code>ec2:DescribeInstances</code>)</h3>
    <p>
      To verify that <code>lab6-viewer</code> is correctly permitted to inspect cloud resources without mutating them:
    </p>
    <ol>
      <li>Maintained selection on User: <code>lab6-viewer</code> in the IAM Policy Simulator.</li>
      <li>Selected Service: <strong>EC2</strong> and Action: <code>DescribeInstances</code>.</li>
      <li>Clicked <strong>Run Simulation</strong>.</li>
    </ol>
    <p>
      <strong>Evaluation Result:</strong> The simulator returned <span class="badge badge-success">Allowed</span> under <strong>Explicit allow</strong> through the attached <code>ReadOnlyAccess</code> managed policy. This proves that viewing and monitoring operations succeed, providing perfect read-only isolation.
    </p>

    <div class="free-img">
      <img src="{step7_b64}" alt="Step 7 - Viewer Allowed to Describe Instances">
    </div>
    <p class="caption">Figure 7: IAM Policy Simulator testing <code>lab6-viewer</code> executing <code>ec2:DescribeInstances</code> &mdash; Result: Allowed (Explicit allow).</p>
  </div>

  <!-- ==========================================================================
       PAGE 15: STEP 8 (POLICY SIMULATOR - OPERATOR DENY S3)
       ========================================================================== -->
  <div class="page">
    <h3>Step 8 &mdash; Test: Custom Policy Blocks Actions Outside Its Scope (<code>s3:CreateBucket</code>)</h3>
    <p>
      To validate that the custom least-privilege policy <code>lab6-ec2-operator</code> strictly confines user capabilities and rejects unauthorized actions outside its defined domain:
    </p>
    <ol>
      <li>Selected User: <code>lab6-operator</code> in the IAM Policy Simulator.</li>
      <li>Selected Service: <strong>S3</strong> and Action: <code>CreateBucket</code>.</li>
      <li>Clicked <strong>Run Simulation</strong>.</li>
    </ol>
    <p>
      <strong>Evaluation Result:</strong> The simulator returned <span class="badge badge-danger">Denied</span> under <strong>Implicit deny</strong>. Because <code>lab6-ec2-operator</code> explicitly permits only EC2 Describe, Start, and Stop actions, any attempt to manipulate Amazon S3 buckets is automatically rejected by the IAM Policy Engine.
    </p>

    <div class="free-img">
      <img src="{step8_b64}" alt="Step 8 - Operator Denied S3 Actions">
    </div>
    <p class="caption">Figure 8: IAM Policy Simulator testing <code>lab6-operator</code> executing <code>s3:CreateBucket</code> &mdash; Result: Denied (Implicit deny).</p>
  </div>

  <!-- ==========================================================================
       PAGE 16: STEP 9 (MFA), TEST MATRIX, OCI COMPARISON & CONCLUSION
       ========================================================================== -->
  <div class="page">
    <h3>Step 9 &mdash; Multi-Factor Authentication (MFA) Setup &amp; Policy Enforcement</h3>
    <p>
      To satisfy enterprise hardening standards, MFA is configured for IAM identities to ensure credentials cannot be exploited via single-factor breaches:
    </p>
    <ol>
      <li>
        <strong>MFA Device Enrollment Procedure:</strong>
        <ul style="margin-top: 6px; margin-bottom: 8px;">
          <li>In the IAM Console, navigate to <strong>Users &rarr; [Target User] &rarr; Security credentials &rarr; Assign MFA device</strong>.</li>
          <li>Specify device name (e.g., <code>Aditya-Phone-MFA</code>) and select <strong>Authenticator app</strong> (TOTP).</li>
          <li>Scan the generated QR code using Google Authenticator or Microsoft Authenticator.</li>
          <li>Enter two consecutive 6-digit TOTP codes generated 30 seconds apart to synchronize time-based drift, then click <strong>Add MFA</strong>.</li>
        </ul>
      </li>
      <li>
        <strong>Enforcing MFA Programmatically via IAM Policy:</strong>
        <p style="margin-top: 6px; margin-bottom: 6px;">
          Administrators enforce MFA compliance using condition keys. The following policy denies all mutating actions unless an active MFA session is validated:
        </p>
        <pre><code>{{
  "Version": "2012-10-17",
  "Statement": [
    {{
      "Sid": "BlockEverythingUnlessMFA",
      "Effect": "Deny",
      "NotAction": ["iam:CreateVirtualMFADevice", "iam:EnableMFADevice", "iam:ListMFADevices"],
      "Resource": "*",
      "Condition": {{
        "BoolIfExists": {{ "aws:MultiFactorAuthPresent": "false" }}
      }}
    }}
  ]
}}</code></pre>
      </li>
    </ol>

    <h3>Summary: IAM Policy Simulation Test Matrix</h3>
    <table class="styled-table">
      <thead>
        <tr>
          <th>User Identity</th>
          <th>Attached Policy / Role</th>
          <th>Tested API Action</th>
          <th>Expected Outcome</th>
          <th>Simulator Result</th>
          <th>Governing Rule</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>lab6-admin</code></td>
          <td><code>AdministratorAccess</code> (via Group)</td>
          <td><code>ec2:RunInstances</code></td>
          <td>Allowed</td>
          <td><span class="badge badge-success">Allowed</span></td>
          <td>Explicit allow in AdministratorAccess policy</td>
        </tr>
        <tr>
          <td><code>lab6-viewer</code></td>
          <td><code>ReadOnlyAccess</code> (Direct)</td>
          <td><code>ec2:RunInstances</code></td>
          <td>Denied</td>
          <td><span class="badge badge-danger">Denied</span></td>
          <td>Implicit deny (no mutating allow exists)</td>
        </tr>
        <tr>
          <td><code>lab6-viewer</code></td>
          <td><code>ReadOnlyAccess</code> (Direct)</td>
          <td><code>ec2:DescribeInstances</code></td>
          <td>Allowed</td>
          <td><span class="badge badge-success">Allowed</span></td>
          <td>Explicit allow in ReadOnlyAccess policy</td>
        </tr>
        <tr>
          <td><code>lab6-operator</code></td>
          <td><code>lab6-ec2-operator</code> (Custom)</td>
          <td><code>s3:CreateBucket</code></td>
          <td>Denied</td>
          <td><span class="badge badge-danger">Denied</span></td>
          <td>Implicit deny (S3 outside EC2 policy scope)</td>
        </tr>
      </tbody>
    </table>

    <div class="info-box purple">
      <strong>Comparative Note &mdash; Oracle Cloud Infrastructure (OCI) IAM:</strong> In OCI, identities are similarly structured into <em>Users</em> and <em>Groups</em>, governed by <em>Compartments</em>. OCI IAM uses human-readable policy syntax: <code>Allow group &lt;GroupName&gt; to &lt;Verb&gt; &lt;Resource-Type&gt; in compartment &lt;CompartmentName&gt;</code>, where verbs follow a 4-tier hierarchy: <code>inspect</code> &rarr; <code>read</code> &rarr; <code>use</code> &rarr; <code>manage</code>.
    </div>

    <h2>Conclusion &amp; Key Takeaways</h2>
    <p>
      In this laboratory practical, I systematically explored the architectural foundations of Cloud Security through Identity &amp; Access Management (IAM). I investigated the principles of authentication, authorization, and the fundamental differences between Users, Groups, and Roles. By provisioning <code>lab6-admin</code>, <code>lab6-viewer</code>, and <code>lab6-operator</code>, I demonstrated group-based administrative inheritance, managed read-only access, and customer-managed JSON policies enforcing the Principle of Least Privilege (PoLP).
    </p>
    <p>
      Using the AWS IAM Policy Simulator, I empirically validated that administrative identities possess full provisioning authority, read-only identities can inspect resources without mutation capability, and custom operators are strictly quarantined to assigned EC2 operational verbs while being denied access to other services (such as S3). Finally, I studied Multi-Factor Authentication (MFA) mechanisms and policy enforcement models, solidifying essential best practices for securing enterprise cloud infrastructure.
    </p>

    <div style="margin-top: 24px; border-top: 1px solid #cbd5e1; padding-top: 14px;">
      <table style="width: 100%; border-collapse: collapse; font-family: 'Times New Roman', Times, serif;">
        <tr>
          <td style="width: 50%; text-align: left; vertical-align: bottom;">
            <strong>Student Signature:</strong> Aditya Chandrajit Deore<br>
            <strong>Date:</strong> 17th October 2026<br>
            <strong>PRN:</strong> 124B1F116 &nbsp;&nbsp;&nbsp;&nbsp; <strong>Batch:</strong> B3
          </td>
          <td style="width: 50%; text-align: right; vertical-align: bottom;">
            <strong>Faculty Assessment:</strong> _______________________<br>
            <strong>Marks / Grade:</strong> _______________________<br>
            <strong>Signature with Seal:</strong> _______________________
          </td>
        </tr>
      </table>
    </div>
  </div>

</div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Successfully generated {html_path} and {index_path} ({len(html)} bytes)!")
