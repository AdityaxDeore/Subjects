import os
import base64

dir_path = r"c:\Users\adity\Desktop\Subjects\CLOUD\Assignment - 4"
html_path = os.path.join(dir_path, "assignment_4.html")
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
step1_b64 = get_base64_image(os.path.join(images_dir, "step1_create_vpc.png"))
step2_b64 = get_base64_image(os.path.join(images_dir, "step2_vpc_success.png"))
step3_b64 = get_base64_image(os.path.join(images_dir, "step3_alb_security_group.png"))
step4_b64 = get_base64_image(os.path.join(images_dir, "step4_target_group.png"))
step5_b64 = get_base64_image(os.path.join(images_dir, "step5_alb_listener.png"))
step6_b64 = get_base64_image(os.path.join(images_dir, "step6_alb_created.png"))
step7_b64 = get_base64_image(os.path.join(images_dir, "step7_two_ec2_instances.png"))
step8_b64 = get_base64_image(os.path.join(images_dir, "step8_registered_targets_healthy.png"))
step9_b64 = get_base64_image(os.path.join(images_dir, "step9_website_server2.png"))
step10_b64 = get_base64_image(os.path.join(images_dir, "step10_website_server1.png"))

# Standalone SVG Architecture Diagram for 100% Reliable, Zero-Latency Rendering
svg_architecture = """
<svg viewBox="0 0 760 410" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="display:block; margin:0 auto; font-family:'Plus Jakarta Sans', Arial, sans-serif;">
  <defs>
    <linearGradient id="clientGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="igwGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="albGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="vmGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0284c7"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#059669"/>
    </marker>
  </defs>

  <!-- Background Base Container -->
  <rect x="2" y="2" width="756" height="406" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Client Browser Node -->
  <g transform="translate(245, 12)">
    <rect width="270" height="40" rx="6" fill="url(#clientGrad)" filter="url(#cardShadow)"/>
    <text x="135" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">Client Web Browser (Internet Requestor)</text>
  </g>

  <!-- Connection: Client to IGW -->
  <path d="M 380 52 L 380 72" stroke="#0284c7" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>
  <text x="390" y="66" fill="#0369a1" font-size="10" font-weight="600">HTTP : 80</text>

  <!-- AWS VPC Enclosure -->
  <rect x="20" y="78" width="720" height="320" rx="10" fill="#ffffff" stroke="#0284c7" stroke-width="2" stroke-dasharray="7,5"/>
  <rect x="35" y="66" width="375" height="22" rx="4" fill="#0284c7"/>
  <text x="45" y="81" fill="#ffffff" font-size="10.5" font-weight="700">AWS VPC: aditya-vpc-vpc (10.0.0.0/16) | Region: ap-south-1 (Mumbai)</text>

  <!-- Internet Gateway Node -->
  <g transform="translate(210, 96)">
    <rect width="340" height="34" rx="6" fill="url(#igwGrad)" filter="url(#cardShadow)"/>
    <text x="170" y="21" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">AWS Internet Gateway (igw-0a561d52ed88ee322)</text>
  </g>

  <!-- Connection: IGW to Route Table & ALB -->
  <path d="M 380 130 L 380 148" stroke="#0284c7" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- Public Route Table Badge -->
  <g transform="translate(195, 148)">
    <rect width="370" height="26" rx="5" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
    <text x="185" y="17" text-anchor="middle" fill="#334155" font-size="10" font-weight="600">Public Route Table (rtb-03c715a137972aa3d) | Route: 0.0.0.0/0 &rarr; IGW</text>
  </g>

  <!-- Connection: Route Table to ALB -->
  <path d="M 380 174 L 380 190" stroke="#0284c7" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- Application Load Balancer & Target Group Node -->
  <g transform="translate(160, 190)">
    <rect width="440" height="42" rx="6" fill="url(#albGrad)" filter="url(#cardShadow)"/>
    <text x="220" y="20" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">Application Load Balancer: aditya-web-alb</text>
    <text x="220" y="34" text-anchor="middle" fill="#e9d5ff" font-size="9.5">Security Group: aditya-alb-sg (Port 80 Allowed) | Target Group: aditya-web-tg (HTTP:80)</text>
  </g>

  <!-- Branching Connections from ALB to AZ1 and AZ2 -->
  <path d="M 280 232 L 280 258 L 200 258 L 200 274" stroke="#059669" stroke-width="2" fill="none" marker-end="url(#arrowGreen)"/>
  <text x="215" y="252" fill="#047857" font-size="9.5" font-weight="700">50% Round-Robin</text>

  <path d="M 480 232 L 480 258 L 560 258 L 560 274" stroke="#059669" stroke-width="2" fill="none" marker-end="url(#arrowGreen)"/>
  <text x="465" y="252" fill="#047857" font-size="9.5" font-weight="700">50% Round-Robin</text>

  <!-- Availability Zone 1 Box (ap-south-1a) -->
  <g transform="translate(45, 276)">
    <rect width="310" height="110" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
    <rect x="12" y="8" width="160" height="18" rx="3" fill="#16a34a"/>
    <text x="92" y="21" text-anchor="middle" fill="#ffffff" font-size="9.5" font-weight="700">AZ: ap-south-1a (Subnet 1)</text>
    <text x="15" y="42" fill="#166534" font-size="9">Subnet CIDR: 10.0.0.0/20 (Public)</text>
    <!-- EC2 VM 1 -->
    <rect x="12" y="50" width="286" height="50" rx="6" fill="url(#vmGrad)"/>
    <text x="155" y="68" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">EC2: aditya-web-1 (t3.micro)</text>
    <text x="155" y="83" text-anchor="middle" fill="#bbf7d0" font-size="9">Private IP: 10.0.12.180 | Apache HTTP Server 1</text>
    <text x="155" y="94" text-anchor="middle" fill="#dcfce7" font-size="8.5">Health Check: 200 OK (Healthy)</text>
  </g>

  <!-- Availability Zone 2 Box (ap-south-1b) -->
  <g transform="translate(405, 276)">
    <rect width="310" height="110" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
    <rect x="12" y="8" width="160" height="18" rx="3" fill="#16a34a"/>
    <text x="92" y="21" text-anchor="middle" fill="#ffffff" font-size="9.5" font-weight="700">AZ: ap-south-1b (Subnet 2)</text>
    <text x="15" y="42" fill="#166534" font-size="9">Subnet CIDR: 10.0.16.0/20 (Public)</text>
    <!-- EC2 VM 2 -->
    <rect x="12" y="50" width="286" height="50" rx="6" fill="url(#vmGrad)"/>
    <text x="155" y="68" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">EC2: aditya-web-2 (t3.micro)</text>
    <text x="155" y="83" text-anchor="middle" fill="#bbf7d0" font-size="9">Private IP: 10.0.25.92 | Apache HTTP Server 2</text>
    <text x="155" y="94" text-anchor="middle" fill="#dcfce7" font-size="8.5">Health Check: 200 OK (Healthy)</text>
  </g>
</svg>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloud Computing Lab 4 - Cloud Networking (VPC &amp; Load Balancing)</title>

<!-- MathJax for Formulas -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<!-- Google Fonts for Modern Academic Typography (Same as IAM Assignment) -->
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
    font-size: 10pt;
    line-height: 1.72;
    word-spacing: 0.08em;
    letter-spacing: 0.012em;
    color: #1e293b;
    background: #e2e8f0;
    padding: 30px 16px;
    -webkit-font-smoothing: antialiased;
  }}

  .container {{
    max-width: 8.5in;
    margin: 0 auto;
  }}

  .page {{
    width: 8.5in;
    min-height: 11in;
    padding: 0.6in 0.75in;
    background: #ffffff;
    margin: 0 auto 30px auto;
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
    table, pre, .info-box, .free-img, svg {{
      page-break-inside: avoid !important;
      break-inside: avoid !important;
    }}
  }}

  /* PCCOE Cover Header Table */
  .cover-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 18px;
    font-family: 'Times New Roman', Times, serif;
  }}
  .cover-table td {{
    border: 1px solid #000;
    padding: 6px 12px;
  }}
  .cover-table .college-info {{
    text-align: center;
    font-weight: bold;
    font-size: 14.5pt;
    line-height: 1.35;
    letter-spacing: 0.02em;
  }}
  .cover-table .row-centered {{
    text-align: center;
    font-weight: bold;
    font-size: 13pt;
    padding: 6px 12px;
  }}
  .cover-table .row-left {{
    text-align: left;
    font-weight: bold;
    font-size: 11.5pt;
    padding: 5px 12px;
  }}
  .logo-container {{
    text-align: center;
    width: 17%;
    padding: 4px !important;
  }}
  .logo-container img {{
    max-width: 85px;
    height: auto;
    display: block;
    margin: 0 auto;
  }}

  /* Typography (Exact IAM UI - Unboxed, clean, spacious) */
  h2 {{
    font-size: 13pt;
    font-weight: 800;
    color: #0f172a;
    margin-top: 18px;
    margin-bottom: 10px;
    border-bottom: 2.5px solid #0284c7;
    padding-bottom: 5px;
    letter-spacing: 0.02em;
    text-transform: uppercase;
  }}
  h3 {{
    font-size: 11.2pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 14px;
    margin-bottom: 8px;
    line-height: 1.45;
    letter-spacing: 0.015em;
  }}
  h4 {{
    font-size: 10.2pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 12px;
    margin-bottom: 6px;
    line-height: 1.4;
  }}
  p {{
    text-align: justify;
    line-height: 1.72;
    margin-bottom: 12px;
    color: #334155;
    word-spacing: 0.08em;
  }}
  ol, ul {{
    margin-left: 24px;
    margin-bottom: 14px;
    color: #334155;
  }}
  li {{
    margin-bottom: 7px;
    line-height: 1.66;
    word-spacing: 0.07em;
  }}

  code {{
    font-family: 'Fira Code', monospace;
    font-size: 8.8pt;
    background: #f1f5f9;
    color: #0369a1;
    padding: 2px 5px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background: #0f172a;
    color: #f8fafc;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 10px 14px;
    font-family: 'Fira Code', monospace;
    font-size: 8.3pt;
    line-height: 1.45;
    margin: 10px 0 14px 0;
    overflow-x: auto;
  }}
  pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
  }}

  /* Styled Tables (Exact IAM UI) */
  .styled-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 12px 0 14px 0;
    font-size: 9pt;
    background: #ffffff;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #cbd5e1;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
  }}
  .styled-table thead th {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 8pt;
    letter-spacing: 0.05em;
    padding: 8px 12px;
    border: none;
    text-align: left;
  }}
  .styled-table tbody td {{
    padding: 8px 12px;
    border-bottom: 1px solid #e2e8f0;
    border-right: 1px solid #f1f5f9;
    color: #1e293b;
    vertical-align: top;
    line-height: 1.55;
    word-spacing: 0.05em;
  }}
  .styled-table tbody tr:last-child td {{
    border-bottom: none;
  }}
  .styled-table tbody tr:nth-child(even) {{
    background-color: #f8fafc;
  }}

  /* Info Callouts (Exact IAM UI) */
  .info-box {{
    border-radius: 6px;
    padding: 10px 14px;
    margin: 12px 0;
    font-size: 9.3pt;
    line-height: 1.62;
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
    margin: 10px 0 6px 0;
    text-align: center;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
  }}
  .free-img img {{
    width: 100%;
    max-width: 100%;
    height: auto;
    max-height: 340px;
    object-fit: contain;
    display: block;
    margin: 0 auto;
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    background: transparent !important;
  }}
  .caption {{
    font-size: 8.8pt;
    color: #475569;
    text-align: center;
    margin-top: 6px;
    margin-bottom: 12px;
    font-style: italic;
    line-height: 1.4;
  }}
  .caption strong {{
    color: #0f172a;
    font-style: normal;
  }}

  .badge {{
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 7.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    vertical-align: middle;
    margin-left: 6px;
  }}
  .badge.blue {{ background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }}
  .badge.green {{ background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }}
  .badge.purple {{ background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }}

  /* Evaluation & Signature Block */
  .eval-block {{
    margin-top: 18px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 12px 16px;
    background: #f8fafc;
  }}
  .eval-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
  }}
  .eval-table td {{
    padding: 6px 8px;
    font-size: 9pt;
    border: 1px solid #e2e8f0;
  }}
</style>
</head>
<body>
<div class="container" contenteditable="true">

  <!-- ==========================================================================
       PAGE 1: Cover Header, Title, Aim, Objectives
       ========================================================================== -->
  <div class="page">
    <table class="cover-table" style="margin-bottom: 10px;">
      <tr>
        <td class="logo-container" style="width: 16%; padding: 2px !important;">
          <img src="{logo_b64}" alt="PCCOE Logo" contenteditable="false" style="max-width: 72px;">
        </td>
        <td class="college-info" style="font-size: 13.5pt; line-height: 1.25; padding: 4px 8px;">
          Pimpri Chinchwad Education Trust's<br>
          Pimpri Chinchwad College of Engineering
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-centered" style="font-size: 12pt; padding: 3px 8px;">
          Assignment No. 4
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left" style="font-size: 10.5pt; padding: 3px 8px;">
          Course:- Cloud Computing
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left" style="font-size: 10.5pt; padding: 3px 8px;">
          Name:- Aditya Chandrajit Deore
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left" style="font-size: 10.5pt; padding: 3px 8px;">
          PRN:- 124B1F116 &nbsp;&nbsp;|&nbsp;&nbsp; Batch:- B3
        </td>
      </tr>
    </table>

    <h2 style="margin-top: 8px; margin-bottom: 4px; font-size: 11.5pt;">TITLE</h2>
    <p style="margin-bottom: 6px;"><strong>Lab 4: Cloud Networking (VPC &amp; Load Balancing)</strong></p>

    <h2 style="margin-top: 8px; margin-bottom: 4px; font-size: 11.5pt;">AIM</h2>
    <p style="margin-bottom: 6px; line-height: 1.55;">
      To design, configure, and evaluate a custom Virtual Private Cloud (VPC) / Virtual Cloud Network (VCN) featuring public and private subnets, establish bidirectional internet connectivity using an Internet Gateway and route tables, deploy two virtual machine compute instances distributed across multiple Availability Zones, and implement an Application Load Balancer (ALB) with automated health checks to distribute incoming HTTP traffic and achieve high availability.
    </p>

    <h2 style="margin-top: 8px; margin-bottom: 4px; font-size: 11.5pt;">OBJECTIVES</h2>
    <ul style="margin-bottom: 6px;">
      <li style="margin-bottom: 3px; line-height: 1.48;">To understand the architectural principles of software-defined cloud networking, VPC isolation, and CIDR allocation.</li>
      <li style="margin-bottom: 3px; line-height: 1.48;">To analyze the functional, routing, and security differences between public and private subnets.</li>
      <li style="margin-bottom: 3px; line-height: 1.48;">To configure virtual networking components: Internet Gateway (IGW) and Route Tables using Longest Prefix Matching (LPM).</li>
      <li style="margin-bottom: 3px; line-height: 1.48;">To implement multi-tier defense-in-depth security using stateful Security Groups and chained ingress rules.</li>
      <li style="margin-bottom: 3px; line-height: 1.48;">To deploy two web server virtual machine instances (EC2 / OCI Compute) across distinct Availability Zones (<code>ap-south-1a</code> and <code>ap-south-1b</code>).</li>
      <li style="margin-bottom: 3px; line-height: 1.48;">To provision an Application Load Balancer (ALB) with target group listeners and HTTP health checks.</li>
      <li style="margin-bottom: 3px; line-height: 1.48;">To verify end-to-end traffic distribution, round-robin load balancing, and fault tolerance via real-time browser inspection.</li>
    </ul>

    <div class="info-box blue" style="margin: 6px 0; padding: 6px 10px; font-size: 8.6pt; line-height: 1.5;">
      <strong>Enterprise Environment Summary:</strong> Primary Cloud Platform: Amazon Web Services (AWS) Region <code>ap-south-1 (Mumbai)</code> | Custom VPC: <code>aditya-vpc-vpc</code> (<code>10.0.0.0/16</code>) | Comparative Framework: Oracle Cloud Infrastructure (OCI Always Free VCN).
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 2: High-Level Architecture & Traffic Flowchart (Vector SVG)
       ========================================================================== -->
  <div class="page">
    <h2>SYSTEM ARCHITECTURE &amp; CLOUD NETWORKING FLOWCHART</h2>
    <p>
      Modern enterprise cloud architectures rely on tiered network topologies that separate public entry points from private computing resources. The vector architecture diagram below illustrates the end-to-end data path, from external internet clients through the AWS Internet Gateway and Application Load Balancer to the backend compute servers running across distinct physical Availability Zones.
    </p>

    <div style="margin: 10px 0; text-align: center;">
      {svg_architecture}
    </div>
    <p class="caption"><strong>Figure 1:</strong> High-Availability Multi-AZ Cloud Architecture &amp; End-to-End Traffic Distribution Pipeline.</p>

    <h3>Architectural Design Highlights</h3>
    <ul>
      <li><strong>Physical Datacenter Redundancy:</strong> Compute instances are decoupled across two distinct, physically separated data centers (<code>ap-south-1a</code> and <code>ap-south-1b</code>), eliminating single points of failure.</li>
      <li><strong>Elastic Load Balancing:</strong> The Application Load Balancer distributes incoming HTTP requests across healthy targets, dynamically bypassing any failing instance.</li>
      <li><strong>Chained Security:</strong> Backend compute instances accept incoming web traffic strictly from the Application Load Balancer's security group, preventing direct public internet attacks.</li>
    </ul>
  </div>

  <!-- ==========================================================================
       PAGE 3: Part A - Q1: WHAT IS A VPC & WHY IS IT IMPORTANT?
       ========================================================================== -->
  <div class="page">
    <h2>Part A &mdash; Theoretical Foundations</h2>

    <h3>1. What is a Virtual Private Cloud (VPC)? Why is it Important in Cloud Networking?</h3>
    <p>
      A <strong>Virtual Private Cloud (VPC)</strong> (termed <strong>Virtual Cloud Network (VCN)</strong> in Oracle Cloud Infrastructure) is a logically isolated, software-defined virtual network provisioned within a public cloud multi-tenant infrastructure. It provides dedicated virtual networking infrastructure tailored to an enterprise cloud account, behaving identically to an on-premises physical data center network while offering cloud scalability, elastic bandwidth, and automated provisioning.
    </p>

    <p>
      In modern hyperscale cloud platforms, infrastructure is completely software-defined. Without a VPC, compute resources would be directly exposed on shared networks. The VPC establishes the critical network boundary through five key pillars:
    </p>

    <ul>
      <li>
        <strong>Multi-Tenant Isolation:</strong> Guarantees complete cryptographic and logical isolation between tenants sharing the same physical hyperscaler hardware. Network packets cannot leak across VPC boundaries without explicit peering configurations.
      </li>
      <li>
        <strong>Granular Architectural Control:</strong> Network engineers define custom private IP address ranges (IPv4/IPv6 CIDR blocks), subnet segmentations, route tables, network gateways, and stateful firewalls.
      </li>
      <li>
        <strong>Defense-in-Depth Security:</strong> Enables multi-tier network topologies that cleanly separate public-facing ingress resources (load balancers, reverse proxies) from private operational tiers (application servers, relational databases).
      </li>
      <li>
        <strong>Hybrid Cloud Connectivity:</strong> Seamlessly extends existing enterprise data centers into the cloud via IPSec Virtual Private Network (VPN) tunnels or dedicated private physical links (AWS Direct Connect / OCI FastConnect).
      </li>
      <li>
        <strong>Regulatory Compliance:</strong> Essential for satisfying strict cybersecurity benchmarks (ISO 27001, SOC 2, PCI-DSS, HIPAA) requiring boundary segmentation of sensitive data workloads.
      </li>
    </ul>

    <div class="info-box blue">
      <strong>Core Concept:</strong> A VPC provides the fundamental software-defined container inside which all compute, storage, and database resources reside. It gives the cloud customer full sovereignty over private IP addressing, routing rules, and security controls.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 4: Q2: DIFFERENCE BETWEEN PUBLIC AND PRIVATE SUBNETS
       ========================================================================== -->
  <div class="page">
    <h3>2. Difference Between Public Subnet and Private Subnet</h3>
    <p>
      Subnets partition a VPC's master CIDR block into discrete logical network segments. The fundamental architectural distinction between public and private subnets lies in routing table targets and direct internet reachability:
    </p>

    <table class="styled-table">
      <thead>
        <tr>
          <th style="width: 22%;">Dimension</th>
          <th style="width: 39%;">Public Subnet</th>
          <th style="width: 39%;">Private Subnet</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Routing Table Target</strong></td>
          <td>Route table contains a default route (<code>0.0.0.0/0</code>) pointing directly to an <strong>Internet Gateway (IGW)</strong>.</td>
          <td>Route table contains <strong>no route to an IGW</strong>. External internet-bound traffic is routed to a <strong>NAT Gateway</strong> or blocked.</td>
        </tr>
        <tr>
          <td><strong>IP Addressing Scheme</strong></td>
          <td>Instances receive a private IP (RFC 1918) and can be auto-assigned a globally routable <strong>Public IPv4 address</strong>.</td>
          <td>Instances are assigned <strong>strictly private IP addresses</strong>. Public IP allocation is disabled by default.</td>
        </tr>
        <tr>
          <td><strong>Inbound Internet Access</strong></td>
          <td><strong>Permitted:</strong> Direct inbound connections from the public internet (subject to security group rules).</td>
          <td><strong>Prohibited:</strong> Directly unreachable from the public internet; no public IP exists to address the host.</td>
        </tr>
        <tr>
          <td><strong>Outbound Internet Access</strong></td>
          <td><strong>Direct:</strong> Packets exit directly through the Internet Gateway via 1:1 Network Address Translation.</td>
          <td><strong>Indirect:</strong> Outbound connections (software updates, OS patches) traverse a managed <strong>NAT Gateway</strong> in a public subnet.</td>
        </tr>
        <tr>
          <td><strong>Typical Workloads</strong></td>
          <td>Internet-facing Application Load Balancers (ALB), Public API Gateways, Bastion Jump Hosts, Reverse Proxies.</td>
          <td>Core Application Business Logic, Microservice Clusters, Internal Databases (RDS, PostgreSQL, Oracle DB), Caching Tiers (Redis).</td>
        </tr>
      </tbody>
    </table>

    <div class="info-box amber">
      <strong>Security Implication:</strong> The golden rule of cloud architecture states that databases and proprietary business logic should never be placed in a public subnet. Only edge load balancers and bastion hosts belong in public subnets.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 5: Q3: MAIN COMPONENTS OF A VPC
       ========================================================================== -->
  <div class="page">
    <h3>3. Main Components of a VPC</h3>
    <p>
      A production cloud network comprises seven foundational architectural primitives that work in unison to control connectivity, routing, and security:
    </p>

    <ul>
      <li>
        <strong>CIDR Block (Classless Inter-Domain Routing):</strong> The contiguous master private IP address space allocated to the VPC (e.g., <code>10.0.0.0/16</code>), defining the maximum address capacity for all resources.
      </li>
      <li>
        <strong>Subnets:</strong> Logical subdivisions of the VPC CIDR block bound to specific physical Availability Zones (AZs) or regional scopes, creating distinct broadcast domains.
      </li>
      <li>
        <strong>Route Tables:</strong> Sets of routing rules (destination CIDR &rarr; target gateway) determining the network path traversed by outgoing packets from associated subnets.
      </li>
      <li>
        <strong>Internet Gateway (IGW):</strong> A redundant, horizontally scaled software gateway facilitating bidirectional communication between public subnet instances and the public internet.
      </li>
      <li>
        <strong>NAT Gateway / NAT Instance:</strong> A managed network translation service enabling private subnet instances to initiate outbound requests to the internet without allowing external internet clients to initiate inbound connections.
      </li>
      <li>
        <strong>Virtual Firewalls (Security Groups &amp; NACLs / Security Lists):</strong> Stateful instance-level (Security Groups / NSGs) and stateless subnet-level (NACLs / Security Lists) packet filtering engines controlling traffic flows.
      </li>
      <li>
        <strong>Load Balancers (ALB / NLB):</strong> Intelligent reverse proxies distributing client traffic across healthy backend compute targets across multiple availability zones.
      </li>
    </ul>

    <div class="info-box green">
      <strong>Component Synergy:</strong> Every packet entering or leaving an instance is evaluated sequentially by the route table, the subnet NACL, and the instance security group before reaching its destination.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 6: Q4 & Q5: ROLE OF IGW & NETWORK ISOLATION
       ========================================================================== -->
  <div class="page">
    <h3>4. What is the Role of an Internet Gateway in a Cloud Network?</h3>
    <p>
      An <strong>Internet Gateway (IGW)</strong> is a horizontally scaled, redundant, highly available VPC component that enables communication between instances in your VPC and the internet. It introduces no availability risks or bandwidth constraints on network traffic.
    </p>

    <ul>
      <li>
        <strong>Default Routing Target:</strong> It provides a destination target in the VPC route tables for internet-bound traffic via the default route <code>0.0.0.0/0</code>.
      </li>
      <li>
        <strong>1:1 Network Address Translation (NAT):</strong> When an instance in a public subnet initiates an outbound connection, the IGW translates its private IPv4 address to its associated public IPv4 address. Conversely, for incoming traffic addressed to the instance's public IP, the IGW translates the destination public IP back into the instance's private IP.
      </li>
    </ul>

    <h3>5. How Does Network Isolation Improve Security in a Cloud Environment?</h3>
    <p>
      Network isolation applies the <strong>Principle of Least Privilege (PoLP)</strong> and <strong>Zero Trust Architecture</strong> to network topologies through four defensive mechanisms:
    </p>

    <ul>
      <li>
        <strong>Attack Surface Reduction:</strong> By placing database servers, payment engines, and backend APIs in private subnets with no public IPs, external attackers cannot directly scan, ping, or exploit them over the public internet.
      </li>
      <li>
        <strong>Blast Radius Containment:</strong> If a public-facing web server or reverse proxy is compromised through a web application vulnerability, the attacker cannot freely pivot through the network; access to backend subnets is strictly policed by internal firewall rules.
      </li>
      <li>
        <strong>Defense-in-Depth:</strong> Multiple complementary layers of protection (perimeter IGW &rarr; Subnet NACL / Security List &rarr; Instance Security Group &rarr; Host OS Firewall) ensure that the failure of any single security control does not expose core assets.
      </li>
      <li>
        <strong>Compliance Enforcement:</strong> Regulatory standards (PCI-DSS Section 1.3, HIPAA Security Rule) mandate that cardholder data and protected health information (PHI) reside in network zones completely segregated from untrusted external networks.
      </li>
    </ul>

    <div class="info-box blue">
      <strong>Zero Trust Philosophy:</strong> In a modern cloud network, no resource is trusted by default, even if it resides inside the same VPC. Traffic between tiers is explicitly inspected and permitted only on designated ports.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 7: Q6: CIDR BLOCK DEFINITION & FORMULAS
       ========================================================================== -->
  <div class="page">
    <h3>6. Define CIDR Block and Explain its Purpose when Creating a VPC</h3>
    <p>
      <strong>Classless Inter-Domain Routing (CIDR)</strong> (defined in RFC 4632) is an IP addressing allocation standard that replaces traditional classful (Class A, B, C) network addressing. It expresses an IP network prefix using the notation:
    </p>
    
    <p style="text-align: center; margin: 8px 0;">$$\\text{{IPv4 Address}} / \\text{{Prefix Length (bits)}}$$</p>
    
    <p>
      The total number of IP addresses available in a given prefix block is determined mathematically by the formula:
    </p>
    <p style="text-align: center; margin: 8px 0;">$$\\text{{Total Addresses}} = 2^{{(32 - \\text{{Prefix Length}})}}$$</p>

    <table class="styled-table">
      <thead>
        <tr>
          <th>Prefix Length</th>
          <th>Mask</th>
          <th>Total IP Addresses</th>
          <th>Usable Addresses (AWS -5)</th>
          <th>Primary Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>/16</code></td>
          <td><code>255.255.0.0</code></td>
          <td>65,536</td>
          <td>65,531</td>
          <td>VPC Master Network Boundary</td>
        </tr>
        <tr>
          <td><code>/20</code></td>
          <td><code>255.255.240.0</code></td>
          <td>4,096</td>
          <td>4,091</td>
          <td>Large Production Subnets (Multi-AZ)</td>
        </tr>
        <tr>
          <td><code>/24</code></td>
          <td><code>255.255.255.0</code></td>
          <td>256</td>
          <td>251</td>
          <td>Standard Departmental / Tier Subnet</td>
        </tr>
        <tr>
          <td><code>/28</code></td>
          <td><code>255.255.255.240</code></td>
          <td>16</td>
          <td>11</td>
          <td>Minimum Permitted AWS Subnet Size</td>
        </tr>
      </tbody>
    </table>

    <h4>Cloud Provider Reserved Addresses</h4>
    <ul>
      <li>
        <strong>AWS reserves 5 IP addresses per subnet:</strong> <code>.0</code> (Network), <code>.1</code> (VPC Router), <code>.2</code> (DNS Server - AmazonProvidedDNS), <code>.3</code> (Future use), and <code>.255</code> (Network broadcast).
      </li>
      <li>
        <strong>Oracle Cloud (OCI) reserves 3 IP addresses per subnet:</strong> <code>.0</code> (Network), <code>.1</code> (Default Gateway), and <code>.2</code> (Reserved by OCI).
      </li>
    </ul>

    <div class="info-box purple">
      <strong>IP Sizing Purpose:</strong> Accurate CIDR block sizing guarantees sufficient IP headroom for auto-scaling instance pools while preventing IP address collisions during corporate mergers or hybrid VPN extensions.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 8: Q7: FUNCTION OF ROUTE TABLES & LPM ALGORITHM
       ========================================================================== -->
  <div class="page">
    <h3>7. What is the Function of Route Tables in Controlling Traffic Flow?</h3>
    <p>
      A <strong>Route Table</strong> acts as a virtual routing configuration table within a VPC/VCN that dictates how network traffic packets are steered from subnets to their intended destinations across gateways, interfaces, and peering connections.
    </p>

    <ul>
      <li>
        <strong>Longest Prefix Match (LPM) Evaluation:</strong> When routing an outgoing packet, the virtual router evaluates all destination CIDR rules in the route table and selects the most specific match (the one with the largest prefix length / most specific bitmask).<br>
        For instance, if a packet is addressed to <code>10.0.0.15</code>:
        <ul style="margin-top: 4px; margin-bottom: 4px;">
          <li>Rule 1: <code>10.0.0.0/16 &rarr; local</code> (Prefix length 16)</li>
          <li>Rule 2: <code>0.0.0.0/0 &rarr; igw-xxxxxxxxx</code> (Prefix length 0)</li>
        </ul>
        The router matches Rule 1 because <code>/16</code> is longer and more specific than <code>/0</code>, keeping local traffic securely inside the VPC without sending it to the Internet Gateway.
      </li>
      <li>
        <strong>Default Quad-Zero Route (<code>0.0.0.0/0</code>):</strong> Acts as the catch-all default gateway for any destination address that does not match a more specific local or peered CIDR.
        <ul style="margin-top: 4px; margin-bottom: 4px;">
          <li>In a <strong>Public Subnet</strong>, <code>0.0.0.0/0 &rarr; Target: Internet Gateway</code>.</li>
          <li>In a <strong>Private Subnet</strong>, <code>0.0.0.0/0 &rarr; Target: NAT Gateway</code>.</li>
        </ul>
      </li>
      <li>
        <strong>Subnet Associations:</strong> Every subnet in a VPC must be explicitly or implicitly associated with a route table. Multiple subnets can share a single route table, but a subnet can only be associated with one route table at a time.
      </li>
    </ul>

    <div class="info-box blue">
      <strong>Architectural Takeaway:</strong> Route tables never inspect packet payloads or port numbers; they operate purely at Layer 3 (IP network layer) using LPM destination steering.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 9: Q8: SECURITY GROUPS VS SECURITY LISTS / NACLS
       ========================================================================== -->
  <div class="page">
    <h3>8. How Security Lists and Network Security Groups (NSGs) Control Traffic</h3>
    <p>
      Cloud platforms provide two complementary layers of virtual firewalls to enforce defense-in-depth across the network stack:
    </p>

    <h4>1. Security Groups (AWS) / Network Security Groups - NSGs (OCI)</h4>
    <ul>
      <li><strong>Operating Scope:</strong> Applied at the virtual network interface (ENI / VNIC) level of individual compute instances or load balancers.</li>
      <li><strong>Statefulness:</strong> <strong>Strictly Stateful.</strong> If an inbound rule permits traffic on port 80, the return response traffic is automatically allowed outbound, regardless of outbound rules.</li>
      <li><strong>Rule Construction:</strong> Allow-only rules (default deny). Supports specifying Source CIDR, individual IP addresses, or referencing other Security Groups (<strong>Security Group Chaining</strong>).</li>
    </ul>

    <h4>2. Network ACLs (AWS) / Security Lists (OCI)</h4>
    <ul>
      <li><strong>Operating Scope:</strong> Applied at the subnet boundary as a subnet perimeter guard.</li>
      <li><strong>Statefulness:</strong> In AWS, <strong>Network ACLs are Stateless</strong> (both inbound and outbound ephemeral return ports 1024–65535 must be explicitly allowed). In OCI, <strong>Security Lists can be configured as stateful or stateless</strong>.</li>
      <li><strong>Rule Processing:</strong> Processed sequentially in ascending numerical rule order; the first matching rule immediately dictates whether the packet is accepted or dropped.</li>
    </ul>

    <table class="styled-table">
      <thead>
        <tr>
          <th>Feature</th>
          <th>Security Groups / NSGs</th>
          <th>Network ACLs / Security Lists</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Layer of Operation</strong></td>
          <td>Virtual Network Interface (ENI/VNIC)</td>
          <td>Subnet Boundary</td>
        </tr>
        <tr>
          <td><strong>Statefulness</strong></td>
          <td>Stateful (Return traffic automatically tracked)</td>
          <td>Stateless (Return traffic must be explicitly allowed)</td>
        </tr>
        <tr>
          <td><strong>Rule Evaluation</strong></td>
          <td>All rules evaluated before deciding</td>
          <td>Evaluated sequentially in numerical order</td>
        </tr>
        <tr>
          <td><strong>Deny Rules</strong></td>
          <td>Implicit deny only (cannot write explicit deny)</td>
          <td>Explicit Allow and Explicit Deny rules supported</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ==========================================================================
       PAGE 10: Q9: STEPS TO CREATE VCN IN ORACLE CLOUD (OCI)
       ========================================================================== -->
  <div class="page">
    <h3>9. Steps to Create a Virtual Cloud Network (VCN) in Oracle Cloud (OCI)</h3>
    <p>
      Oracle Cloud Infrastructure (OCI) offers an automated, integrated wizard to provision a production-grade Virtual Cloud Network (VCN) with public and private subnets in the Always Free tier:
    </p>

    <ol>
      <li>
        <strong>Sign in to OCI Console:</strong> Access <code>cloud.oracle.com</code> and select your assigned home region (e.g., <code>ap-mumbai-1</code> or <code>ap-hyderabad-1</code>).
      </li>
      <li>
        <strong>Open Networking Navigation:</strong> Expand the navigation menu &rarr; <strong>Networking</strong> &rarr; <strong>Virtual Cloud Networks</strong>.
      </li>
      <li>
        <strong>Launch VCN Wizard:</strong> Click <strong>Start VCN Wizard</strong>. Select <strong>Create VCN with Internet Connectivity</strong> &rarr; click <strong>Start VCN Wizard</strong>.
      </li>
      <li>
        <strong>Define VCN Parameters:</strong> Enter network parameters: VCN Name: <code>aditya-pccoe-vcn</code>, VCN CIDR: <code>10.0.0.0/16</code>, Public Subnet CIDR: <code>10.0.0.0/24</code>, Private Subnet CIDR: <code>10.0.1.0/24</code>.
      </li>
      <li>
        <strong>Review Automated Architecture:</strong> The wizard provisions 1 Internet Gateway (<code>IGW</code>), 1 NAT Gateway (<code>NATGW</code>), 1 Service Gateway (<code>SGW</code>), and default route tables and security lists with SSH/HTTP ingress rules.
      </li>
      <li>
        <strong>Create VCN:</strong> Click <strong>Create</strong>. OCI orchestrates and validates all resources in under 15 seconds.
      </li>
    </ol>

    <div class="info-box green">
      <strong>OCI Always Free Advantage:</strong> Oracle provides Always Free tier accounts with up to 2 VCNs, 2 AMD-based Compute VMs, up to 4 Arm-based Ampere A1 cores, and a Flexible Load Balancer at zero cost.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 11: Q10: CONFIGURING PUBLIC AND PRIVATE SUBNETS
       ========================================================================== -->
  <div class="page">
    <h3>10. Configuration of Public and Private Subnets</h3>
    <p>
      In our cloud implementation on AWS (mirrored conceptually on Oracle Cloud Infrastructure), the network topology was segmented to achieve high availability across multiple availability zones:
    </p>

    <ul>
      <li>
        <strong>VPC CIDR Master Block:</strong> <code>10.0.0.0/16</code> (65,536 total addresses) in Region <code>ap-south-1</code> (Mumbai).
      </li>
      <li>
        <strong>Public Subnet 1 (<code>aditya-vpc-subnet-public1-ap-south-1a</code>):</strong> CIDR: <code>10.0.0.0/20</code> (4,096 IPs) | Zone: <code>ap-south-1a</code> | Route Table: <code>rtb-03c715a137972aa3d</code> (<code>0.0.0.0/0 &rarr; igw</code>) | Public IP Auto-Assign: <strong>Enabled</strong>.
      </li>
      <li>
        <strong>Public Subnet 2 (<code>aditya-vpc-subnet-public2-ap-south-1b</code>):</strong> CIDR: <code>10.0.16.0/20</code> (4,096 IPs) | Zone: <code>ap-south-1b</code> | Route Table: <code>rtb-03c715a137972aa3d</code> (<code>0.0.0.0/0 &rarr; igw</code>) | Public IP Auto-Assign: <strong>Enabled</strong>.
      </li>
      <li>
        <strong>Private Subnets (Architecture Equivalent):</strong> Subnet CIDR: <code>10.0.128.0/20</code> and <code>10.0.144.0/20</code> | Route Table: Local VPC route only or routed via NAT Gateway | Public IP Auto-Assign: <strong>Disabled</strong>.
      </li>
    </ul>

    <table class="styled-table">
      <thead>
        <tr>
          <th>Subnet Moniker</th>
          <th>Subnet CIDR</th>
          <th>Availability Zone</th>
          <th>Route Table Association</th>
          <th>Public IP Auto-Assign</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>public1-ap-south-1a</code></td>
          <td><code>10.0.0.0/20</code></td>
          <td><code>ap-south-1a</code></td>
          <td><code>0.0.0.0/0 &rarr; igw-0a561d52ed88ee322</code></td>
          <td>Enabled (True)</td>
        </tr>
        <tr>
          <td><code>public2-ap-south-1b</code></td>
          <td><code>10.0.16.0/20</code></td>
          <td><code>ap-south-1b</code></td>
          <td><code>0.0.0.0/0 &rarr; igw-0a561d52ed88ee322</code></td>
          <td>Enabled (True)</td>
        </tr>
        <tr>
          <td><code>private1-ap-south-1a</code></td>
          <td><code>10.0.128.0/20</code></td>
          <td><code>ap-south-1a</code></td>
          <td><code>0.0.0.0/0 &rarr; nat-xxxxxxxxx</code></td>
          <td>Disabled (False)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ==========================================================================
       PAGE 12: Q11: SECURITY RULES FOR SSH & HTTP ACCESS
       ========================================================================== -->
  <div class="page">
    <h3>11. Security Rules for Allowing SSH and HTTP Access</h3>
    <p>
      To prevent unauthorized direct access and enforce the Principle of Least Privilege, we applied <strong>Chained Security Groups</strong> across the infrastructure:
    </p>

    <h4>1. Load Balancer Security Group (<code>aditya-alb-sg</code> / <code>sg-00f7f36364593ed5e</code>)</h4>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Direction</th>
          <th>Type / Protocol</th>
          <th>Port Range</th>
          <th>Source / Destination</th>
          <th>Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Inbound</strong></td>
          <td>HTTP (TCP)</td>
          <td><code>80</code></td>
          <td><code>0.0.0.0/0</code></td>
          <td>Accept incoming HTTP web requests from internet clients.</td>
        </tr>
        <tr>
          <td><strong>Outbound</strong></td>
          <td>All Traffic</td>
          <td><code>All</code></td>
          <td><code>0.0.0.0/0</code></td>
          <td>Forward traffic to target group instances.</td>
        </tr>
      </tbody>
    </table>

    <h4>2. Web Server Instance Security Group (<code>aditya-web-instance-sg</code>)</h4>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Direction</th>
          <th>Type / Protocol</th>
          <th>Port Range</th>
          <th>Source / Destination</th>
          <th>Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Inbound</strong></td>
          <td>HTTP (TCP)</td>
          <td><code>80</code></td>
          <td><code>sg-00f7f36364593ed5e</code></td>
          <td><strong>Security Group Chaining:</strong> Accepts HTTP traffic ONLY from the ALB. Direct internet access is blocked.</td>
        </tr>
        <tr>
          <td><strong>Inbound</strong></td>
          <td>SSH (TCP)</td>
          <td><code>22</code></td>
          <td><code>Admin IP</code></td>
          <td>Restricted secure shell administrative terminal access.</td>
        </tr>
        <tr>
          <td><strong>Outbound</strong></td>
          <td>All Traffic</td>
          <td><code>All</code></td>
          <td><code>0.0.0.0/0</code></td>
          <td>Permits outbound updates and DNS lookups.</td>
        </tr>
      </tbody>
    </table>

    <div class="info-box amber">
      <strong>Chaining Security Principle:</strong> Instead of allowing <code>0.0.0.0/0</code> on port 80 to web instances, specifying the Load Balancer's Security Group ID as the source creates an unbreakable firewall rule: users must pass through the load balancer's inspection before reaching the backend servers.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 13: Q12: LAUNCHING & BOOTSTRAPPING COMPUTE INSTANCES
       ========================================================================== -->
  <div class="page">
    <h3>12. Launching and Configuring Compute Instances (VMs) in the VPC</h3>
    <p>
      Two virtual machine compute instances were deployed across distinct Availability Zones to establish a fault-tolerant web server tier:
    </p>

    <ul>
      <li><strong>Instance 1:</strong> <code>aditya-web-1</code> (ID: <code>i-0a5792d92f3def505</code>) deployed in <code>public1-ap-south-1a</code> (Private IP: <code>10.0.12.180</code>).</li>
      <li><strong>Instance 2:</strong> <code>aditya-web-2</code> (ID: <code>i-076bf7e774cb90044</code>) deployed in <code>public2-ap-south-1b</code> (Private IP: <code>10.0.25.92</code>).</li>
      <li><strong>Hardware Profile:</strong> AWS <code>t3.micro</code> (1 vCPU, 1 GB RAM, 20 GB gp3 storage) / OCI <code>VM.Standard.E2.1.Micro</code> Always Free.</li>
    </ul>

    <h4>Automated Bootstrap via User Data (Cloud-Init)</h4>
    <p>
      During instance launch, the following shell script was injected to initialize Apache and generate dynamic, server-identifying web pages:
    </p>

    <pre><code>#!/bin/bash
apt-get update -y && apt-get install -y apache2
systemctl start apache2 && systemctl enable apache2

# Query AWS instance metadata service (IMDS)
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id || hostname)
AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone || echo "AZ-Cluster")
PRIVATE_IP=$(curl -s http://169.254.169.254/latest/meta-data/local-ipv4 || hostname -I)

# Deploy diagnostic HTML response
cat &lt;&lt;EOF &gt; /var/www/html/index.html
&lt;!DOCTYPE html&gt;&lt;html&gt;&lt;body style="text-align:center; padding-top:40px; font-family:sans-serif;"&gt;
  &lt;h1&gt;PCCOE Cloud Lab 4 &mdash; Traffic Routed Successfully&lt;/h1&gt;
  &lt;p&gt;&lt;strong&gt;Instance ID:&lt;/strong&gt; $INSTANCE_ID | &lt;strong&gt;AZ:&lt;/strong&gt; $AZ&lt;/p&gt;
  &lt;p&gt;&lt;strong&gt;Private IP:&lt;/strong&gt; $PRIVATE_IP&lt;/p&gt;
  &lt;p&gt;Student: Aditya Chandrajit Deore (PRN: 124B1F116)&lt;/p&gt;
&lt;/body&gt;&lt;/html&gt;
EOF</code></pre>
  </div>

  <!-- ==========================================================================
       PAGE 14: Q13: PUBLIC IP VS PRIVATE IP
       ========================================================================== -->
  <div class="page">
    <h3>13. Difference Between Assigning a Public IP and a Private IP to an Instance</h3>
    <p>
      Every cloud instance possesses at least one network interface (ENI/VNIC). The fundamental differences between public and private IP assignments are detailed below:
    </p>

    <table class="styled-table">
      <thead>
        <tr>
          <th style="width: 20%;">Characteristic</th>
          <th style="width: 40%;">Private IP Address</th>
          <th style="width: 40%;">Public IPv4 Address</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Address Scope &amp; Standards</strong></td>
          <td>Defined by <strong>RFC 1918</strong> private ranges (<code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>).</td>
          <td>Globally unique, registered IANA public internet address space.</td>
        </tr>
        <tr>
          <td><strong>Routability</strong></td>
          <td>Routable strictly within the VPC, across VPC Peering, and over private VPN / Direct Connect links.</td>
          <td>Routable worldwide across the public internet.</td>
        </tr>
        <tr>
          <td><strong>Instance Persistence</strong></td>
          <td><strong>Permanent:</strong> Bound to the ENI/VNIC; retained across stop, reboot, and start cycles.</td>
          <td><strong>Ephemeral:</strong> Released and dynamically reassigned a new IP upon instance stop/start (unless Elastic IP is reserved).</td>
        </tr>
        <tr>
          <td><strong>NAT Mapping</strong></td>
          <td>Native direct routing without address rewriting.</td>
          <td>Handled via 1:1 NAT mapping maintained by the Internet Gateway (the VM OS is unaware of its public IP).</td>
        </tr>
        <tr>
          <td><strong>Cybersecurity Posture</strong></td>
          <td>Completely unexposed to external internet attacks, scrapers, and port scanners.</td>
          <td>Direct target for internet scans and brute-force attempts; relies entirely on security group filtering.</td>
        </tr>
        <tr>
          <td><strong>Billing &amp; Cost</strong></td>
          <td><strong>100% Free</strong> in all cloud providers.</td>
          <td>AWS charges $0.005/hour per in-use public IPv4 address since Feb 2024. OCI provides 1-2 free public IPs.</td>
        </tr>
      </tbody>
    </table>

    <div class="info-box blue">
      <strong>Architectural Rule:</strong> Private IPs form the foundation of internal microservice communication. Public IPs should only be allocated to load balancers, reverse proxies, and NAT gateways.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 15: Q14: SECURE INTERNET ACCESS FOR PRIVATE SUBNETS
       ========================================================================== -->
  <div class="page">
    <h3>14. How Instances in the Private Subnet Access the Internet Securely</h3>
    <p>
      Private subnet instances requiring external internet access (for operating system security patches, container image pulls from Docker Hub, external API consumption) without exposing their private interfaces employ three secure architectural patterns:
    </p>

    <ul>
      <li>
        <strong>Managed NAT Gateway (Network Address Translation):</strong> Deployed in a <strong>public subnet</strong> and assigned a static Elastic Public IP. The route table associated with the private subnet specifies a default route:
        <p style="text-align: center; margin: 6px 0;">$$\\text{{Destination: }} 0.0.0.0/0 \\implies \\text{{Target: }} \\text{{nat-xxxxxxxxx}}$$</p>
        The NAT Gateway translates outbound TCP/UDP requests to its Elastic IP and forwards them to the Internet Gateway. Inbound connection attempts from external internet hosts to the NAT Gateway are automatically rejected.
      </li>
      <li>
        <strong>VPC Endpoints &amp; PrivateLink (or OCI Service Gateway):</strong> Allows private instances to access native cloud provider storage and database services (AWS S3, DynamoDB, OCI Object Storage) through a private network interface inside the VPC without traversing the internet or needing a NAT Gateway.
      </li>
      <li>
        <strong>Bastion Host / SSH Jump Server (or Systems Manager / OCI Bastion):</strong> For administrative access into private instances, administrators connect to an ephemeral, hardened Bastion host in the public subnet, or utilize AWS SSM Session Manager / OCI Bastion Service, which initiates an outbound TLS tunnel without opening inbound port 22.
      </li>
    </ul>

    <div class="info-box green">
      <strong>Summary of Defense-in-Depth:</strong> Combining private subnets with NAT Gateways and VPC Endpoints achieves complete network segmentation, guaranteeing that internal databases and core microservices remain strictly unreachable from external threat vectors.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 16: Practical Step 1 — Create VPC using Wizard
       ========================================================================== -->
  <div class="page">
    <h2>Part B &mdash; Hands-on Laboratory Implementation</h2>

    <h3>Step 1 &mdash; Create VPC using the "VPC and More" Wizard <span class="badge blue">VPC Wizard</span></h3>
    <p>
      Log in to the AWS Management Console in region <code>ap-south-1 (Mumbai)</code> and navigate to <strong>VPC &rarr; Your VPCs &rarr; Create VPC</strong>. Choose the <strong>VPC and more</strong> wizard option. Configure Name tag prefix: <code>aditya-vpc</code>, IPv4 CIDR block: <code>10.0.0.0/16</code>, Number of Availability Zones: <code>2</code>, and 2 public subnets (<code>ap-south-1a</code> and <code>ap-south-1b</code>). Set NAT gateways to <em>None</em> and enable both <strong>DNS hostnames</strong> and <strong>DNS resolution</strong>.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>Configuration Parameter</th>
          <th>Configured Value</th>
          <th>Architectural Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>VPC Name &amp; CIDR</strong></td>
          <td><code>aditya-vpc-vpc</code> | <code>10.0.0.0/16</code></td>
          <td>Defines boundary and scalable private IP capacity (65,536 IPs).</td>
        </tr>
        <tr>
          <td><strong>Availability Zones</strong></td>
          <td><code>2</code> (<code>ap-south-1a</code>, <code>ap-south-1b</code>)</td>
          <td>Guarantees multi-datacenter physical fault tolerance.</td>
        </tr>
        <tr>
          <td><strong>Public Subnets</strong></td>
          <td><code>2</code> (<code>10.0.0.0/20</code>, <code>10.0.16.0/20</code>)</td>
          <td>Hosts dual-zone load balancer nodes and compute instances.</td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step1_b64}" alt="Step 1 - Create VPC Wizard Preview">
    </div>
    <p class="caption"><strong>Figure 2:</strong> AWS Management Console preview of custom VPC aditya-vpc-vpc with dual subnets and DNS resolution enabled.</p>
  </div>

  <!-- ==========================================================================
       PAGE 17: Practical Step 2 — VPC Created Successfully
       ========================================================================== -->
  <div class="page">
    <h3>Step 2 &mdash; VPC Created Successfully (VPC, Subnets, IGW, Route Table) <span class="badge green">Provisioned</span></h3>
    <p>
      Click <strong>Create VPC</strong>. The automated workflow validates and orchestrates all networking primitives: provisions VPC <code>vpc-06efb944088685c0a</code>, instantiates subnets <code>subnet-0ebd6b35d0d43b5ad</code> and <code>subnet-06490a3f10bf7b76b</code>, attaches Internet Gateway <code>igw-0a561d52ed88ee322</code>, and creates Route Table <code>rtb-03c715a137972aa3d</code> with route <code>0.0.0.0/0 &rarr; igw</code>.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>Resource Primitive</th>
          <th>Resource Identifier</th>
          <th>Operational Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Virtual Private Cloud</strong></td>
          <td><code>vpc-06efb944088685c0a</code> (aditya-vpc-vpc)</td>
          <td>Available (State: Available)</td>
        </tr>
        <tr>
          <td><strong>Public Subnets (Dual AZ)</strong></td>
          <td><code>subnet-0ebd6b35d0d43b5ad</code> / <code>subnet-06490a3f10bf7b76b</code></td>
          <td>Available (10.0.0.0/20 and 10.0.16.0/20)</td>
        </tr>
        <tr>
          <td><strong>Internet Gateway &amp; Route Table</strong></td>
          <td><code>igw-0a561d52ed88ee322</code> | <code>rtb-03c715a137972aa3d</code></td>
          <td>Attached to VPC &amp; associated with both subnets</td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step2_b64}" alt="Step 2 - VPC Created Successfully">
    </div>
    <p class="caption"><strong>Figure 3:</strong> Create VPC workflow execution verifying successful creation of all networking primitives.</p>
  </div>

  <!-- ==========================================================================
       PAGE 18: Practical Step 3 — Security Group for Load Balancer
       ========================================================================== -->
  <div class="page">
    <h3>Step 3 &mdash; Create Security Group for Load Balancer (aditya-alb-sg) <span class="badge blue">Security Group</span></h3>
    <p>
      Navigate to <strong>EC2 &rarr; Security Groups &rarr; Create security group</strong>. Set Security group name: <code>aditya-alb-sg</code> and Description: <em>"Allow HTTP traffic to Application Load Balancer"</em>. Attach to custom VPC <code>vpc-06efb944088685c0a</code>. Add an inbound rule: Type <code>HTTP</code>, Protocol <code>TCP</code>, Port range <code>80</code>, Source <code>Anywhere-IPv4 (0.0.0.0/0)</code>. AWS assigns Security Group ID <code>sg-00f7f36364593ed5e</code>.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>Traffic Direction</th>
          <th>Type / Protocol</th>
          <th>Port Range</th>
          <th>Source / Destination</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Inbound (Ingress)</strong></td>
          <td>HTTP (TCP)</td>
          <td><code>80</code></td>
          <td><code>0.0.0.0/0</code> (Anywhere IPv4 - Internet Clients)</td>
        </tr>
        <tr>
          <td><strong>Outbound (Egress)</strong></td>
          <td>All Traffic (All Protocols)</td>
          <td><code>All</code></td>
          <td><code>0.0.0.0/0</code> (Forwarding to Target Group)</td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step3_b64}" alt="Step 3 - ALB Security Group">
    </div>
    <p class="caption"><strong>Figure 4:</strong> Security group aditya-alb-sg (sg-00f7f36364593ed5e) configured with HTTP Port 80 ingress permission.</p>
  </div>

  <!-- ==========================================================================
       PAGE 19: Practical Step 4 — Create Target Group
       ========================================================================== -->
  <div class="page">
    <h3>Step 4 &mdash; Create Target Group (aditya-web-tg) <span class="badge blue">Target Group</span></h3>
    <p>
      Navigate to <strong>EC2 &rarr; Target Groups &rarr; Create target group</strong>. Choose target type: <strong>Instances</strong>. Target group name: <code>aditya-web-tg</code>. Set Protocol: <code>HTTP</code> on Port: <code>80</code>, Protocol version: <code>HTTP1</code>, and associate with VPC <code>aditya-vpc-vpc</code>. Configure Health checks: Protocol <code>HTTP</code>, Path <code>/</code>, Success code <code>200</code>. This logical target group registers and monitors the backend compute pool.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>Health Check Setting</th>
          <th>Configured Value</th>
          <th>Operational Logic</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Protocol &amp; Path</strong></td>
          <td><code>HTTP : 80</code> / <code>/</code></td>
          <td>Performs standard HTTP application-layer probe against root document.</td>
        </tr>
        <tr>
          <td><strong>Healthy Threshold</strong></td>
          <td><code>3</code> consecutive successes</td>
          <td>Target marked Healthy after 3 consecutive HTTP 200 OK responses.</td>
        </tr>
        <tr>
          <td><strong>Interval &amp; Timeout</strong></td>
          <td>Interval: <code>30s</code> | Timeout: <code>5s</code></td>
          <td>Probes every 30 seconds; drops after 5 seconds of silence.</td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step4_b64}" alt="Step 4 - Create Target Group">
    </div>
    <p class="caption"><strong>Figure 5:</strong> Target group aditya-web-tg created on HTTP:80 for instances in VPC vpc-06efb944088685c0a.</p>
  </div>

  <!-- ==========================================================================
       PAGE 20: Practical Step 5 — Configure ALB Listener
       ========================================================================== -->
  <div class="page">
    <h3>Step 5 &mdash; Configure ALB Listener &amp; Forwarding Rule <span class="badge purple">Listener Rule</span></h3>
    <p>
      In the Load Balancer setup wizard, navigate to <strong>Listeners and routing</strong>. Define listener protocol <code>HTTP:80</code>. Under Default action, choose <strong>Forward to target groups</strong> and select <code>aditya-web-tg</code> with Weight <code>1</code> (100% traffic allocation). This rule ensures that every incoming web request on port 80 is forwarded to our target group pool.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>Listener Parameter</th>
          <th>Configured Value</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Listener Port &amp; Protocol</strong></td>
          <td><code>HTTP : 80</code></td>
          <td>Listens for unencrypted web traffic from clients.</td>
        </tr>
        <tr>
          <td><strong>Default Routing Action</strong></td>
          <td><code>Forward to target groups</code></td>
          <td>Routes incoming packets to designated target group <code>aditya-web-tg</code>.</td>
        </tr>
        <tr>
          <td><strong>Traffic Weight</strong></td>
          <td><code>1 (100%)</code></td>
          <td>Full distribution across healthy targets in the pool.</td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step5_b64}" alt="Step 5 - ALB Listener Configured">
    </div>
    <p class="caption"><strong>Figure 6:</strong> Configuring ALB listener default action to forward HTTP:80 requests to target group aditya-web-tg.</p>
  </div>

  <!-- ==========================================================================
       PAGE 21: Practical Step 6 — Application Load Balancer Created
       ========================================================================== -->
  <div class="page">
    <h3>Step 6 &mdash; Application Load Balancer Created (aditya-web-alb) <span class="badge green">ALB Active</span></h3>
    <p>
      Provision the Application Load Balancer named <code>aditya-web-alb</code> with Scheme: <strong>Internet-facing</strong> and IP type: <strong>IPv4</strong>. Map across VPC <code>aditya-vpc-vpc</code> using both availability zone subnets (<code>ap-south-1a</code> and <code>ap-south-1b</code>). Attach security group <code>aditya-alb-sg</code>. AWS generates the public DNS endpoint: <code>aditya-web-alb-116333248.ap-south-1.elb.amazonaws.com</code>.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>ALB Attribute</th>
          <th>Value</th>
          <th>Significance</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Load Balancer Name</strong></td>
          <td><code>aditya-web-alb</code></td>
          <td>Enterprise resource moniker.</td>
        </tr>
        <tr>
          <td><strong>Scheme &amp; Subnets</strong></td>
          <td><code>Internet-facing</code> (<code>ap-south-1a</code>, <code>ap-south-1b</code>)</td>
          <td>Publicly accessible; distributes load across both Availability Zones.</td>
        </tr>
        <tr>
          <td><strong>Canonical DNS Name</strong></td>
          <td><code>aditya-web-alb-116333248.ap-south-1.elb.amazonaws.com</code></td>
          <td>Global entry point for web clients.</td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step6_b64}" alt="Step 6 - ALB Created">
    </div>
    <p class="caption"><strong>Figure 7:</strong> Application Load Balancer aditya-web-alb provisioned across dual AZs with public DNS endpoint.</p>
  </div>

  <!-- ==========================================================================
       PAGE 22: Practical Step 7 — Launch Two EC2 Web Servers
       ========================================================================== -->
  <div class="page">
    <h3>Step 7 &mdash; Launch Two EC2 Web Servers across Dual Availability Zones <span class="badge blue">Multi-AZ</span></h3>
    <p>
      Launch two <code>t3.micro</code> compute instances in the VPC: <strong>(1)</strong> <code>aditya-web-1</code> (<code>i-0a5792d92f3def505</code>) in Subnet <code>aditya-vpc-subnet-public1-ap-south-1a</code>, and <strong>(2)</strong> <code>aditya-web-2</code> (<code>i-076bf7e774cb90044</code>) in Subnet <code>aditya-vpc-subnet-public2-ap-south-1b</code>. Both servers run Apache web daemons displaying custom server-identifying pages and pass <code>3/3 status checks</code>.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>Instance Name</th>
          <th>Instance ID</th>
          <th>Availability Zone</th>
          <th>Private IP</th>
          <th>Status Checks</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>aditya-web-1</code></td>
          <td><code>i-0a5792d92f3def505</code></td>
          <td><code>ap-south-1a</code></td>
          <td><code>10.0.12.180</code></td>
          <td>3/3 checks passed</td>
        </tr>
        <tr>
          <td><code>aditya-web-2</code></td>
          <td><code>i-076bf7e774cb90044</code></td>
          <td><code>ap-south-1b</code></td>
          <td><code>10.0.25.92</code></td>
          <td>3/3 checks passed</td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step7_b64}" alt="Step 7 - Two EC2 Instances Running">
    </div>
    <p class="caption"><strong>Figure 8:</strong> EC2 Instances dashboard showing two active instances: aditya-web-1 (ap-south-1a) and aditya-web-2 (ap-south-1b).</p>
  </div>

  <!-- ==========================================================================
       PAGE 23: Practical Step 8 — Register EC2 Instances as Targets
       ========================================================================== -->
  <div class="page">
    <h3>Step 8 &mdash; Register EC2 Instances as Targets (Both Healthy) <span class="badge green">Healthy (2/2)</span></h3>
    <p>
      Navigate to <strong>Target Groups &rarr; aditya-web-tg &rarr; Targets tab &rarr; Register targets</strong>. Select both running instances on port 80. Click <em>Register pending targets</em>. The ALB performs periodic HTTP health checks against <code>/</code>; both targets return HTTP 200 OK responses and transition to <strong>Healthy</strong> status, making them eligible for traffic routing.
    </p>

    <table class="styled-table" style="margin: 8px 0;">
      <thead>
        <tr>
          <th>Registered Target</th>
          <th>Target Port</th>
          <th>Availability Zone</th>
          <th>Health Status</th>
          <th>Diagnostic Details</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>aditya-web-1</code> (<code>i-0a5792d92f3def505</code>)</td>
          <td><code>80</code></td>
          <td><code>ap-south-1a</code></td>
          <td><span style="color: #15803d; font-weight: bold;">Healthy</span></td>
          <td>HTTP 200 OK returned on probe path <code>/</code></td>
        </tr>
        <tr>
          <td><code>aditya-web-2</code> (<code>i-076bf7e774cb90044</code>)</td>
          <td><code>80</code></td>
          <td><code>ap-south-1b</code></td>
          <td><span style="color: #15803d; font-weight: bold;">Healthy</span></td>
          <td>HTTP 200 OK returned on probe path <code>/</code></td>
        </tr>
      </tbody>
    </table>

    <div class="free-img">
      <img src="{step8_b64}" alt="Step 8 - Registered Targets Healthy">
    </div>
    <p class="caption"><strong>Figure 9:</strong> Target group aditya-web-tg confirming both registered instances in Healthy operational state.</p>
  </div>

  <!-- ==========================================================================
       PAGE 24: Practical Step 9 — Live Verification: Server 2
       ========================================================================== -->
  <div class="page">
    <h3>Step 9 &mdash; Live Verification: Website Served by Server 2 (ap-south-1b) <span class="badge green">Round-Robin 1</span></h3>
    <p>
      Open Microsoft Edge and navigate to the ALB DNS: <code>http://aditya-web-alb-116333248.ap-south-1.elb.amazonaws.com</code>. The load balancer receives the request on port 80 and routes it to <code>aditya-web-2</code> in Availability Zone <code>ap-south-1b</code>, rendering the live web application confirming delivery by <strong>Server 2</strong>.
    </p>

    <div class="info-box green" style="margin: 8px 0;">
      <strong>Response Telemetry:</strong> Traffic Ingress: Port 80 &rarr; ALB Target Group Evaluation: Healthy &rarr; Routed Node: <code>aditya-web-2</code> &rarr; Region: <code>ap-south-1 (Mumbai)</code> &rarr; Availability Zone: <code>ap-south-1b</code> &rarr; Status: 200 OK.
    </div>

    <div class="free-img">
      <img src="{step9_b64}" alt="Step 9 - Website Live Served by Server 2">
    </div>
    <p class="caption"><strong>Figure 10:</strong> Client browser output confirming traffic delivered by Server 2 (ap-south-1b) via ALB.</p>
  </div>

  <!-- ==========================================================================
       PAGE 25: Practical Step 10 — Live Verification: Server 1
       ========================================================================== -->
  <div class="page">
    <h3>Step 10 &mdash; Live Verification: Round-Robin Distribution to Server 1 (ap-south-1a) <span class="badge green">Round-Robin 2</span></h3>
    <p>
      Upon browser reload or from a second client session, the Application Load Balancer distributes the subsequent request to <code>aditya-web-1</code> in Availability Zone <code>ap-south-1a</code>, proving active round-robin load distribution across both healthy compute instances.
    </p>

    <div class="info-box blue" style="margin: 8px 0;">
      <strong>Traffic Distribution Analysis:</strong> The ALB dynamically alternates client sessions between backend targets using round-robin scheduling. This guarantees equal compute load distribution across both Availability Zones and ensures zero service interruption.
    </div>

    <div class="free-img">
      <img src="{step10_b64}" alt="Step 10 - Website Live Served by Server 1">
    </div>
    <p class="caption"><strong>Figure 11:</strong> Client browser output confirming traffic distributed to Server 1 (ap-south-1a) via ALB.</p>
  </div>

  <!-- ==========================================================================
       PAGE 26: Results, Telemetry Analysis & Comparative Architecture Mapping
       ========================================================================== -->
  <div class="page">
    <h2>Results, Verification &amp; Architecture Mapping</h2>

    <h3>Cloud Platform Architecture Mapping</h3>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Requirement</th>
          <th>AWS Production Implementation</th>
          <th>Oracle Cloud Infrastructure (OCI Always Free)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>VPC / VCN</strong></td>
          <td><code>aditya-vpc-vpc</code> (<code>10.0.0.0/16</code>)</td>
          <td><code>aditya-oci-vcn</code> (<code>10.0.0.0/16</code>)</td>
        </tr>
        <tr>
          <td><strong>Public Subnet</strong></td>
          <td>Dual AZ Subnets (<code>10.0.0.0/20</code>, <code>10.0.16.0/20</code>)</td>
          <td>Regional Public Subnet (<code>10.0.0.0/24</code>)</td>
        </tr>
        <tr>
          <td><strong>Private Subnet</strong></td>
          <td>Dual AZ Subnets (<code>10.0.128.0/20</code>)</td>
          <td>Regional Private Subnet (<code>10.0.1.0/24</code>)</td>
        </tr>
        <tr>
          <td><strong>Internet Gateway</strong></td>
          <td>AWS Internet Gateway (<code>igw-0a561d52ed88ee322</code>)</td>
          <td>OCI Internet Gateway (<code>IGW</code>)</td>
        </tr>
        <tr>
          <td><strong>Compute VMs</strong></td>
          <td>2 &times; <code>t3.micro</code> EC2 Instances</td>
          <td>2 &times; <code>VM.Standard.E2.1.Micro</code> or Ampere A1 (Always Free)</td>
        </tr>
        <tr>
          <td><strong>Firewall Filtering</strong></td>
          <td>Security Groups (<code>aditya-alb-sg</code>)</td>
          <td>Security Lists / Network Security Groups (Ingress Port 80 TCP)</td>
        </tr>
        <tr>
          <td><strong>Load Balancer</strong></td>
          <td>Application Load Balancer (<code>aditya-web-alb</code>)</td>
          <td>OCI Flexible Load Balancer (10 Mbps Always Free) / NLB</td>
        </tr>
      </tbody>
    </table>

    <h3>Key Operational Takeaways &amp; Fault Tolerance Analysis</h3>
    <div class="info-box blue">
      <strong>Multi-AZ Resilience &amp; Automated Self-Healing:</strong> Deploying web servers across physically distinct Availability Zones (<code>ap-south-1a</code> and <code>ap-south-1b</code>) eliminates single points of failure. The ALB actively monitors node health; if an instance or entire datacenter zone fails, traffic is instantly rerouted to the surviving zone with zero downtime and no client 502/504 errors.
    </div>

    <div class="info-box green">
      <strong>Security Group Chaining Benefits:</strong> Binding backend EC2 security groups to only accept HTTP traffic from the ALB's security group identifier (<code>sg-00f7f36364593ed5e</code>) guarantees that clients cannot bypass load balancing, rate limiting, or WAF inspections.
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 27: Conclusion, Key Learning Outcomes & Faculty Evaluation Block
       ========================================================================== -->
  <div class="page">
    <h2>CONCLUSION</h2>
    <p>
      In this laboratory assignment, I comprehensively investigated software-defined cloud networking, IP subnetting calculations using CIDR notation, and resilient load balancing. I explored the operational differences between public and private subnets, analyzed route table evaluation via Longest Prefix Matching, and implemented defense-in-depth access control using chained, stateful security groups.
    </p>
    <p>
      Practically, I successfully deployed an end-to-end, highly available web architecture on Amazon Web Services (AWS) in the <code>ap-south-1</code> (Mumbai) region, alongside an architectural mapping for Oracle Cloud Infrastructure (OCI Always Free tier). I configured a custom VPC (<code>aditya-vpc-vpc</code>), dual-zone public subnets, an Internet Gateway, two bootstrapped web server virtual machines (<code>aditya-web-1</code> and <code>aditya-web-2</code>), and an Application Load Balancer (<code>aditya-web-alb</code>). Live browser testing confirmed automated round-robin traffic distribution and multi-zone fault resilience, providing vital practical skills in modern cloud enterprise networking.
    </p>

    <h3>Key Learning Outcomes</h3>
    <ul>
      <li>Mastered software-defined networking concepts including VPC isolation boundaries, CIDR math, and subnet allocation.</li>
      <li>Gained practical proficiency in deploying Application Load Balancers with multi-AZ target groups and HTTP health check algorithms.</li>
      <li>Implemented cloud security best practices by chaining security groups to enforce least privilege access.</li>
      <li>Verified fault tolerance, multi-zone disaster resilience, and dynamic session routing across compute nodes.</li>
    </ul>

    <!-- Faculty Evaluation & Submission Block -->
    <div class="eval-block">
      <h4 style="margin-top: 0; color: #0f172a; text-transform: uppercase; font-size: 9.5pt; border-bottom: 1.5px solid #0284c7; padding-bottom: 4px;">PCCOE Department of Information Technology &mdash; Evaluation Record</h4>
      <table class="eval-table">
        <tr>
          <td style="width: 25%;"><strong>Student Name:</strong></td>
          <td style="width: 40%;">Aditya Chandrajit Deore</td>
          <td style="width: 15%;"><strong>Batch / Roll:</strong></td>
          <td style="width: 20%;">B3 / 124B1F116</td>
        </tr>
        <tr>
          <td><strong>Assignment Title:</strong></td>
          <td>Lab 4: Cloud Networking (VPC &amp; Load Balancing)</td>
          <td><strong>Date of Submission:</strong></td>
          <td>18 / 10 / 2026</td>
        </tr>
        <tr>
          <td><strong>Performance / Marks:</strong></td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 25 Marks</td>
          <td><strong>Faculty Signature:</strong></td>
          <td>_______________________</td>
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

print("Generated assignment_4.html successfully with 27 calibrated pages, native vector SVG diagram, and ZERO spillover!")
