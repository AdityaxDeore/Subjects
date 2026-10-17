import os
import base64

dir_path = r"c:\Users\adity\Desktop\Subjects\CLOUD\Assignment - 5"
html_path = os.path.join(dir_path, "assignment_5.html")
images_dir = os.path.join(dir_path, "images")

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        print(f"Warning: {image_path} not found")
        return ""
    ext = os.path.splitext(image_path)[1].lower().replace(".", "")
    mime = "image/jpeg" if ext in ("jfif", "jpg", "jpeg") else "image/png"
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{data}"

logo_b64 = get_base64_image(os.path.join(dir_path, "pccoelogo.jfif"))

# All 21 practical workflow steps with short concise description & screenshot
steps_data = [
    {
        "num": 1,
        "title": "Launch a Single EC2 Instance (lab5-web-2)",
        "img": "gdoc_step_1.png",
        "desc": "Provisioned an Amazon EC2 instance named <code>lab5-web-2</code> (Instance ID: <code>i-0ff8aef326439e30c</code>, type <code>t3.micro</code>, Amazon Linux 2023) in AWS Mumbai region (<code>ap-south-1b</code>) with public IPv4 assigned.",
        "caption": "Figure 1: AWS Management Console showing the running EC2 virtual machine instance lab5-web-2."
    },
    {
        "num": 2,
        "title": "Configure Instance Name & OS AMI",
        "img": "1name.png",
        "desc": "Configured the instance tag name (<code>lab5-web-2</code>) and selected the 64-bit Amazon Linux 2023 AMI as the base cloud virtual machine operating system.",
        "caption": "Figure 2: Configuring instance name and Amazon Machine Image (AMI)."
    },
    {
        "num": 3,
        "title": "Configure RSA Key Pair for Secure Authentication",
        "img": "keypair4.png",
        "desc": "Selected the RSA key pair (<code>.pem</code> / <code>.ppk</code>) to ensure secure, authenticated terminal access to the cloud virtual machine.",
        "caption": "Figure 3: Selecting RSA key pair authentication credentials for EC2 access."
    },
    {
        "num": 4,
        "title": "Configure VPC Subnet & Public IP Assignment",
        "img": "5network.png",
        "desc": "Placed the instance in the default VPC subnet with <em>Auto-assign public IP</em> enabled to provide external internet connectivity.",
        "caption": "Figure 4: EC2 Network settings and subnet public IPv4 routing configuration."
    },
    {
        "num": 5,
        "title": "Configure Inbound Security Group Firewall Rules",
        "img": "1 security.png",
        "desc": "Configured the cloud virtual firewall (Security Group) rules to authorize inbound HTTP traffic on TCP Port 80 from <code>0.0.0.0/0</code> and SSH management on Port 22.",
        "caption": "Figure 5: Inbound security group rules authorizing Port 80 (HTTP) traffic."
    },
    {
        "num": 6,
        "title": "Verify Instance Running State in EC2 Dashboard",
        "img": "3.console.png",
        "desc": "Confirmed in the EC2 Management Console that instance <code>lab5-web-2</code> passed 2/2 status checks and entered the active <code>Running</code> state.",
        "caption": "Figure 6: EC2 Management Console verifying active running status and public IP."
    },
    {
        "num": 7,
        "title": "Configure PuTTY SSH Connection",
        "img": "putty1.png",
        "desc": "Entered the public IPv4 address of the EC2 virtual machine into PuTTY and configured an SSH connection on destination Port 22.",
        "caption": "Figure 7: PuTTY configuration specifying EC2 public IP and connection port."
    },
    {
        "num": 8,
        "title": "Load Private Key for PuTTY Authentication",
        "img": "putty2.png",
        "desc": "Imported the cryptographic private key into PuTTY SSH Auth credentials to authenticate the remote session.",
        "caption": "Figure 8: Specifying private key credentials for PuTTY SSH authentication."
    },
    {
        "num": 9,
        "title": "Establish Authenticated Terminal Session",
        "img": "7terminal.png",
        "desc": "Successfully established an encrypted SSH terminal connection to the cloud virtual machine shell as <code>ec2-user</code>.",
        "caption": "Figure 9: Authenticated Linux terminal session open on the EC2 virtual machine."
    },
    {
        "num": 10,
        "title": "Update System Package Repositories",
        "img": "1sudo apt updatw.png",
        "desc": "Synchronized package indices and security updates on the virtual machine using <code>sudo dnf update -y</code>.",
        "caption": "Figure 10: Updating Linux package manager indices on the cloud VM."
    },
    {
        "num": 11,
        "title": "Install Apache HTTP Web Server Daemon",
        "img": "2install apcahe.png",
        "desc": "Installed the Apache HTTP Server package (<code>sudo dnf install -y httpd</code>) to handle incoming HTTP requests on Port 80.",
        "caption": "Figure 11: Installing Apache HTTP Server daemon (httpd) on the instance."
    },
    {
        "num": 12,
        "title": "Install Build Tools & Core Dependencies",
        "img": "3install dependencies.png",
        "desc": "Installed runtime build utilities, developer libraries, and system dependencies required for hosting multiple web apps.",
        "caption": "Figure 12: Installing core dependencies and build utilities on the VM."
    },
    {
        "num": 13,
        "title": "Clone Web Application Source Code",
        "img": "cloning git repo.png",
        "desc": "Cloned the web application files into isolated web directory structures to prepare for directory-based multi-hosting.",
        "caption": "Figure 13: Cloning application repository files onto the VM filesystem."
    },
    {
        "num": 14,
        "title": "Install Node.js Runtime Environment",
        "img": "instaling node js.png",
        "desc": "Configured Node.js and NPM package tools on the cloud VM to build modern frontend dependencies and bundle assets.",
        "caption": "Figure 14: Installing Node.js runtime and environment dependencies."
    },
    {
        "num": 15,
        "title": "Install Web Application Package Dependencies",
        "img": "install website depedencies .png",
        "desc": "Executed package dependency installations to prepare all styles, scripts, and runtime packages for the hosted sites.",
        "caption": "Figure 15: Installing web application package dependencies."
    },
    {
        "num": 16,
        "title": "Start & Enable Apache Service Daemon",
        "img": "retart server.png",
        "desc": "Started the Apache web server daemon using <code>sudo systemctl start httpd</code> and configured it to enable automatically on reboot.",
        "caption": "Figure 16: Starting and enabling the Apache HTTP daemon service."
    },
    {
        "num": 17,
        "title": "Deploy Website 1 (Aditya's Portfolio) at /site1/",
        "img": "gdoc_step_2.png",
        "desc": "Deployed Website 1 inside <code>/var/www/html/site1/index.html</code> and verified live browser rendering at <code>http://&lt;public-ip&gt;/site1/</code>.",
        "caption": "Figure 17: Live verification of Website 1 (Aditya's Portfolio) accessed via /site1/."
    },
    {
        "num": 18,
        "title": "Deploy Website 2 (Campus Eats) at /site2/",
        "img": "gdoc_step_3.png",
        "desc": "Deployed Website 2 inside <code>/var/www/html/site2/index.html</code> and verified live browser rendering at <code>http://&lt;public-ip&gt;/site2/</code> on the exact same VM.",
        "caption": "Figure 18: Live verification of Website 2 (Campus Eats) accessed via /site2/."
    },
    {
        "num": 19,
        "title": "Live Browser URL Verification — Website 1",
        "img": "website url.png",
        "desc": "Inspected the live browser URL bar showing the cloud VM's external IP cleanly resolving Website 1 over HTTP Port 80.",
        "caption": "Figure 19: Full browser verification with live IP address resolution for Website 1."
    },
    {
        "num": 20,
        "title": "Live Browser URL Verification — Website 2",
        "img": "website2_url.png",
        "desc": "Inspected the live browser URL bar confirming the exact same cloud VM external IP concurrently serves Website 2 on the second sub-path.",
        "caption": "Figure 20: Full browser verification with live IP address resolution for Website 2."
    },
    {
        "num": 21,
        "title": "Concurrent Multi-Website Verification Summary",
        "img": "website ss.png",
        "desc": "Demonstrated simultaneous, independent operation of both distinct websites hosted on a single cloud virtual machine instance.",
        "caption": "Figure 21: Verification of both websites hosted and served concurrently from a single cloud VM."
    }
]

# Generate Practical Pages (2 steps per page, clean free images without outer cards/boxes)
step_pages_html = ""
for i in range(0, len(steps_data), 2):
    batch = steps_data[i:i+2]
    step_pages_html += """
  <!-- ==========================================================================
       PRACTICAL IMPLEMENTATION PAGE
       ========================================================================== -->
  <div class="page">
"""
    if i == 0:
        step_pages_html += """    <h2>Part B &mdash; Practical Implementation Workflow</h2>
    <p style="margin-bottom: 24px;">
      The following step-by-step reproducible workflow demonstrates launching a single AWS EC2 virtual machine, configuring network ingress firewalls, installing the Apache HTTP web server, and deploying two independent websites (<em>Aditya's Portfolio</em> at <code>/site1/</code> and <em>Campus Eats</em> at <code>/site2/</code>) on the same instance.
    </p>
"""
    for s in batch:
        b64 = get_base64_image(os.path.join(images_dir, s["img"]))
        step_pages_html += f"""
    <div class="step-card">
      <h3>Step {s["num"]} &mdash; {s["title"]}</h3>
      <p>{s["desc"]}</p>
      <img src="{b64}" alt="{s["title"]}" class="free-screenshot">
      <div class="image-caption">{s["caption"]}</div>
    </div>
"""
    step_pages_html += """  </div>
"""

# Assemble Full Clean, Spacious Document
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloud Computing Lab 5 - Deploy Two Different Websites on a Single Cloud-Based VM</title>
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
    font-size: 10.6pt;
    line-height: 1.85;
    word-spacing: 0.12em;
    letter-spacing: 0.02em;
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
    padding: 0.8in 0.9in;
    background: #ffffff;
    margin: 0 auto 36px auto;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.1), 0 8px 12px -6px rgba(0, 0, 0, 0.05);
    position: relative;
    box-sizing: border-box;
    border-radius: 4px;
  }}

  .page:focus-within {{
    outline: 2px dashed #0284c7;
  }}

  @media print {{
    body {{
      background: #ffffff !important;
      padding: 0 !important;
    }}
    .container {{
      max-width: 100% !important;
      margin: 0 !important;
      box-shadow: none !important;
    }}
    .page {{
      width: 100% !important;
      min-height: auto !important;
      margin: 0 !important;
      padding: 0.48in 0.55in !important;
      box-shadow: none !important;
      border: none !important;
      page-break-after: always !important;
      break-after: page !important;
      border-radius: 0 !important;
    }}
    .step-card, .free-screenshot, .image-caption, .styled-table, .info-box {{
      break-inside: avoid !important;
      page-break-inside: avoid !important;
    }}
  }}

  /* PCCOE Cover Header Table */
  .cover-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 26px;
    font-family: 'Times New Roman', Times, serif;
  }}
  .cover-table td {{
    border: 1px solid #000;
    padding: 9px 15px;
  }}
  .cover-table .college-info {{
    text-align: center;
    font-weight: bold;
    font-size: 15.5pt;
    line-height: 1.45;
    letter-spacing: 0.02em;
  }}
  .cover-table .row-centered {{
    text-align: center;
    font-weight: bold;
    font-size: 13.8pt;
    padding: 9px 15px;
  }}
  .cover-table .row-left {{
    text-align: left;
    font-weight: bold;
    font-size: 12.8pt;
    padding: 8px 15px;
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
    margin-top: 28px;
    margin-bottom: 16px;
    border-bottom: 2.5px solid #0284c7;
    padding-bottom: 6px;
    letter-spacing: 0.025em;
    text-transform: uppercase;
  }}
  h3 {{
    font-size: 11.8pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 24px;
    margin-bottom: 12px;
    line-height: 1.55;
    letter-spacing: 0.015em;
  }}
  h4 {{
    font-size: 10.8pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 18px;
    margin-bottom: 10px;
    line-height: 1.55;
  }}
  p {{
    text-align: justify;
    line-height: 1.85;
    margin-bottom: 18px;
    color: #334155;
    word-spacing: 0.12em;
    letter-spacing: 0.02em;
  }}
  ol, ul {{
    margin-left: 28px;
    margin-bottom: 20px;
    color: #334155;
  }}
  li {{
    margin-bottom: 12px;
    line-height: 1.8;
    word-spacing: 0.1em;
    letter-spacing: 0.015em;
  }}

  code {{
    font-family: 'Fira Code', monospace;
    font-size: 9pt;
    background: #f1f5f9;
    color: #0369a1;
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
    letter-spacing: 0;
  }}

  /* Styled Tables */
  .styled-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 20px 0 24px 0;
    font-size: 9.4pt;
    background: #ffffff;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #cbd5e1;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
  }}
  .styled-table thead th {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 8.4pt;
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
    line-height: 1.65;
    word-spacing: 0.06em;
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
    padding: 14px 18px;
    margin: 20px 0;
    font-size: 9.8pt;
    line-height: 1.75;
    border-left: 4.5px solid;
    word-spacing: 0.08em;
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

  /* Step Card Container */
  .step-card {{
    margin-bottom: 28px;
    break-inside: avoid;
  }}
  .step-card h3 {{
    margin-top: 14px;
    margin-bottom: 10px;
  }}
  .step-card p {{
    margin-bottom: 12px;
  }}

  /* FREE SCREENSHOT STYLING (NO OUTER BOX / NO CANVAS / BIG & CLEAN) */
  .free-screenshot {{
    width: 100%;
    max-width: 100%;
    height: auto;
    max-height: 295px;
    display: block;
    margin: 10px auto 6px auto;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  }}

  .image-caption {{
    font-size: 8.8pt;
    color: #475569;
    text-align: center;
    margin-top: 6px;
    margin-bottom: 20px;
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
          Assignment / Laboratory Practical No. 5
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
    <p style="font-size: 11.2pt; margin-bottom: 10px;">
      <strong>Lab 5:</strong> Deploy Two Different Websites on a Single Cloud-Based Virtual Machine Instance.
    </p>
    <p style="margin-bottom: 22px;">
      <span class="badge badge-aws">Cloud Platform: Amazon Web Services (AWS)</span> &bull; 
      <strong>Region:</strong> <code>ap-south-1</code> (Mumbai) &bull; 
      <strong>Compute Service:</strong> Amazon Elastic Compute Cloud (EC2)
    </p>

    <h2>Aim</h2>
    <p>
      To understand the core virtualization architecture of cloud computing, analyze physical versus virtual server trade-offs, explore web hosting request-routing flows, and practically configure and host two independent websites on a single cloud-based virtual machine instance using directory-based virtual hosting on an Apache web server.
    </p>

    <h2>Objectives</h2>
    <ol>
      <li>To define a Virtual Machine (VM) in a cloud infrastructure and study its hypervisor-managed abstraction layers.</li>
      <li>To compare the technical, operational, and financial differences between physical bare-metal servers and virtual cloud servers.</li>
      <li>To evaluate the core architectural advantages of deploying modern web applications on cloud VMs.</li>
      <li>To define web hosting and trace the end-to-end HTTP request resolution lifecycle in a cloud virtualized network.</li>
      <li>To understand multi-hosting (virtual hosting) concepts and examine how a web server segregates concurrent incoming client requests.</li>
      <li>To analyze the three primary multi-hosting methodologies: port-based, name-based (domains/subdomains), and directory/path-based hosting.</li>
      <li>To practically deploy two independent websites (<em>Aditya's Portfolio</em> at <code>/site1/</code> and <em>Campus Eats</em> at <code>/site2/</code>) on a single AWS EC2 instance (<code>lab5-web-2</code>) and verify live browser access.</li>
    </ol>
  </div>

  <!-- ==========================================================================
       PAGE 2: PART A - Q1 (VIRTUAL MACHINE IN CLOUD) & Q2 (PHYSICAL VS VIRTUAL)
       ========================================================================== -->
  <div class="page">
    <h2>Part A &mdash; Theoretical Foundations</h2>

    <h3>1. What is a Virtual Machine (VM) in a Cloud Environment?</h3>
    <p>
      A <strong>Virtual Machine (VM)</strong> in a cloud environment is an isolated, software-emulated computing system that executes on shared physical hardware within a cloud provider's hyperscale data center. A low-level software abstraction layer known as a <strong>hypervisor</strong> (or Virtual Machine Monitor &mdash; VMM) partitions the underlying physical host's CPU, memory, storage disks, and network interfaces into multiple isolated virtual computing environments, each executing its own independent guest operating system (e.g., Linux, Windows Server).
    </p>
    <p>
      In the cloud, a VM (such as an <strong>Amazon Elastic Compute Cloud &mdash; EC2</strong> instance) is provisioned on demand in minutes through an automated web management console, Command Line Interface (CLI), or Infrastructure as Code (IaC) API. Cloud VMs are elastic &mdash; they can be resized (vertically scaled), stopped, snapshotted, and terminated dynamically, and organizations are billed strictly for the compute hours or seconds the instance actively runs.
    </p>

    <div class="info-box blue">
      <strong>Key Concept:</strong> Cloud VMs provide strong multi-tenancy and OS-level isolation. While multiple customer instances share physical hardware blades, no tenant can inspect, modify, or interfere with neighboring memory spaces or disk I/O.
    </div>

    <h3>2. Difference Between a Physical Server and a Virtual Server</h3>
    <p>
      A <strong>physical server</strong> (bare-metal) is a single, dedicated hardware machine comprising physical CPU sockets, RAM modules, motherboard chipsets, and physical network adapters. An operating system is installed directly onto this hardware, granting applications exclusive access to physical resources. When traffic is low, unused capacity sits completely idle, resulting in wasted capital.
    </p>
    <p>
      A <strong>virtual server</strong> (Virtual Machine), conversely, is a software-defined slice of shared hardware created by a hypervisor. Multiple virtual servers run concurrently on the same physical host, each executing an independent guest OS. They are provisioned in minutes, highly elastic, portable via disk images/snapshots, and billed on a utility model.
    </p>
  </div>

  <!-- ==========================================================================
       PAGE 3: COMPARISON TABLE & Q3 (ADVANTAGES OF CLOUD VMS)
       ========================================================================== -->
  <div class="page">
    <h3>Comparison: Physical Server vs. Virtual Server</h3>
    <table class="styled-table">
      <thead>
        <tr>
          <th style="width: 20%;">Parameter</th>
          <th style="width: 40%;">Physical Server (Bare-Metal)</th>
          <th style="width: 40%;">Virtual Server (Cloud-Based VM)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Hardware Coupling</strong></td>
          <td>Tightly coupled to specific physical chips, disks, and vendor BIOS/firmware.</td>
          <td>Completely decoupled from hardware; operates on standardized virtual hypervisor interfaces.</td>
        </tr>
        <tr>
          <td><strong>Provisioning Time</strong></td>
          <td>Slow; requires physical procurement, cabling, mounting, and manual OS setup (days to weeks).</td>
          <td>Near-instantaneous; automated provisioning via console or API in seconds using pre-built AMIs.</td>
        </tr>
        <tr>
          <td><strong>Scalability &amp; Elasticity</strong></td>
          <td>Rigid; upgrades necessitate ordering and physically inserting new RAM sticks or CPU blades.</td>
          <td>Highly elastic; instance types can be resized up/down, or horizontally auto-scaled in minutes.</td>
        </tr>
        <tr>
          <td><strong>Cost Structure</strong></td>
          <td>Heavy upfront Capital Expenditure (CapEx) for hardware, cooling, rack space, and power.</td>
          <td>Flexible Operational Expenditure (OpEx) with pay-as-you-go per-second/hour utility billing.</td>
        </tr>
        <tr>
          <td><strong>Resource Utilization</strong></td>
          <td>Typically low (10%&ndash;25% average utilization), resulting in stranded capacity and idle power draw.</td>
          <td>High efficiency; hypervisors pack multiple workloads onto one physical host (&gt;75% utilization).</td>
        </tr>
        <tr>
          <td><strong>Disaster Recovery</strong></td>
          <td>Hardware failure causes total downtime until replacement parts arrive; manual tape/disk backups.</td>
          <td>Trivial recovery; instant point-in-time EBS snapshots, multi-AZ replication, and AMI rebuilding.</td>
        </tr>
        <tr>
          <td><strong>Maintenance</strong></td>
          <td>In-house engineers must physically service fans, drives, power supplies, and firmware updates.</td>
          <td>Cloud provider fully maintains physical hardware, facility power, cooling, and network links.</td>
        </tr>
      </tbody>
    </table>

    <h3>3. Advantages of Deploying Web Applications on Cloud-Based VMs</h3>
    <ul>
      <li><strong>Elasticity &amp; Dynamic Scaling:</strong> Scale compute capacity up or down automatically based on real-time traffic demand (e.g., via AWS Auto Scaling Groups), preventing crashes during traffic surges without permanent over-provisioning.</li>
      <li><strong>Cost Optimization:</strong> Eliminates large upfront capital investments. Customers pay strictly for compute time used and can stop or terminate staging/test instances when idle.</li>
      <li><strong>High Availability &amp; Resilience:</strong> Web servers can be easily deployed across multiple isolated Availability Zones (AZs) within a region, ensuring high availability even if a physical data center suffers an outage.</li>
      <li><strong>Rapid Deployment Speed:</strong> Production-ready server instances with hardened Linux kernels and pre-configured web stacks can be launched in minutes from custom or community Amazon Machine Images (AMIs).</li>
      <li><strong>Global Reach &amp; Low Latency:</strong> Applications can be deployed in cloud data centers globally close to end users, minimizing network latency.</li>
    </ul>
  </div>

  <!-- ==========================================================================
       PAGE 4: Q4 (WEB HOSTING IN CLOUD) & ARCHITECTURE DIAGRAM
       ========================================================================== -->
  <div class="page">
    <h3>4. Define Web Hosting. How Does It Work in a Cloud Setup?</h3>
    <p>
      <strong>Web Hosting</strong> is the foundational internet service of storing a website's files (HTML documents, stylesheets, client scripts, media, and backend code) on an Internet-connected server and serving them to client web browsers over standard application-layer protocols (HTTP/HTTPS).
    </p>

    <h4>Operational Lifecycle of Web Hosting in a Cloud VM Setup:</h4>
    <p>
      In a cloud setup, web hosting decouples physical facility management from application serving through a coordinated sequence of virtualization, cloud networking, and web server daemons:
    </p>

    <ol>
      <li><strong>Website Asset Storage:</strong> The website's source code and static assets reside on a cloud virtual machine's persistent storage volume (e.g., an AWS Elastic Block Store &mdash; EBS volume mounted at <code>/var/www/html/</code>) running an HTTP web server daemon such as Apache (<code>httpd</code>) or Nginx.</li>
      <li><strong>IP Assignment &amp; Routing:</strong> The cloud VM is provisioned with a private IPv4 address within a Virtual Private Cloud (VPC) subnet and assigned a public IPv4 address mapped through an AWS Internet Gateway (IGW).</li>
      <li><strong>DNS Resolution:</strong> When an end user enters a domain name (or directly inputs the VM's public IP into a browser), the Domain Name System (DNS) resolves the human-readable hostname to the cloud VM's external public IP address.</li>
      <li><strong>Cloud Ingress Firewall Filtering:</strong> The incoming TCP connection packet arrives at the AWS edge and is evaluated by the instance's <strong>Security Group</strong> (a stateful virtual firewall). If an inbound rule allows traffic on destination Port 80 (HTTP) or Port 443 (HTTPS), the packet passes to the virtual network interface.</li>
      <li><strong>Web Server Processing &amp; Response:</strong> The web server parses the HTTP request headers, identifies the requested URI path (e.g., <code>/site1/</code> vs <code>/site2/</code>), reads the asset, and returns the response payload (<code>HTTP/1.1 200 OK</code>) back to the browser.</li>
    </ol>
  </div>

  <!-- ==========================================================================
       PAGE 5: Q5 (MULTI-HOSTING) & Q6 (WAYS TO HOST MULTIPLE WEBSITES)
       ========================================================================== -->
  <div class="page">
    <h3>5. Concept of Hosting Multiple Websites on One Server (Multi-Hosting)</h3>
    <p>
      <strong>Multi-Hosting</strong> (formally known as <em>Virtual Hosting</em>) is the architectural practice of serving two or more independent websites from a single physical or virtual server and a single IP address. Instead of provisioning an expensive dedicated virtual machine for every distinct website, a single web server daemon (such as Apache HTTP Server or Nginx) inspects each incoming HTTP request and dynamically decides which site's files to serve.
    </p>
    <p>
      The web server differentiates requests based on one of three attributes: the <strong>HTTP <code>Host:</code> header</strong> (domain name), the <strong>TCP destination port number</strong>, or the <strong>URL request path</strong>. Each website maintains its own isolated document root directory, separate configuration rules, and distinct logging streams, allowing them to remain completely independent while sharing the underlying compute CPU, RAM, disk, and network bandwidth &mdash; drastically cutting infrastructure costs.
    </p>

    <h3>6. Possible Ways to Host Multiple Websites on a Single VM</h3>
    <p>
      Modern web servers support three standardized methodologies for hosting multiple websites on a single virtual machine instance:
    </p>

    <h4>(a) Using Different Ports (Port-Based Virtual Hosting)</h4>
    <p>
      The web server daemon binds and listens on multiple distinct TCP port numbers on the same IP address. For example, Website 1 answers on standard Port 80 (<code>http://IP:80/</code>), while Website 2 answers on custom Port 8080 (<code>http://IP:8080/</code>).
    </p>

    <h4>(b) Using Different Domain Names / Subdomains (Name-Based Virtual Hosting)</h4>
    <p>
      Multiple domain names (e.g., <code>site1.com</code> and <code>site2.com</code>) resolve via DNS A-records to the exact same cloud VM IP address, listening on standard ports 80/443. The web server inspects the mandatory HTTP <code>Host:</code> header sent in the browser's request.
    </p>

    <h4>(c) Using Different Directories / Sub-Paths (Path-Based Multi-Hosting)</h4>
    <p>
      Both websites are hosted under a single web server root, segregated into distinct subdirectory folders (e.g., <code>/var/www/html/site1/</code> and <code>/var/www/html/site2/</code>). Browsers access the respective websites via dedicated URL sub-paths: <code>http://&lt;public-ip&gt;/site1/</code> and <code>http://&lt;public-ip&gt;/site2/</code>.
    </p>

    <div class="info-box green">
      <strong>Approach Selected in this Laboratory:</strong> As specified in the lab assignment, we implement <strong>Approach (c) &mdash; Different Directories</strong>. Two independent web applications (<em>Aditya's Portfolio</em> at <code>/site1/</code> and <em>Campus Eats</em> at <code>/site2/</code>) are hosted concurrently on a single Apache instance running on an AWS EC2 VM.
    </div>
  </div>

  <!-- INJECT ALL PRACTICAL STEP PAGES (21 STEPS WITH SCREENSHOTS & DESCRIPTIONS) -->
{step_pages_html}

  <!-- ==========================================================================
       FINAL PAGE: VERIFICATION ANALYSIS, SUMMARY & CONCLUSION
       ========================================================================== -->
  <div class="page">
    <h2>Verification Analysis &amp; Multi-Hosting Summary</h2>
    <p>
      To verify that both websites operate concurrently and independently on the single cloud virtual machine, HTTP client requests were dispatched to all endpoints from external web browsers:
    </p>

    <table class="styled-table">
      <thead>
        <tr>
          <th>Requested URL</th>
          <th>Mapped Filesystem Path</th>
          <th>HTTP Status</th>
          <th>Rendered Application View</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>http://&lt;public-ip&gt;/site1/</code></td>
          <td><code>/var/www/html/site1/index.html</code></td>
          <td><span class="badge badge-success">200 OK</span></td>
          <td>Aditya's Portfolio (Personal software engineering portfolio)</td>
        </tr>
        <tr>
          <td><code>http://&lt;public-ip&gt;/site2/</code></td>
          <td><code>/var/www/html/site2/index.html</code></td>
          <td><span class="badge badge-success">200 OK</span></td>
          <td>Campus Eats (Campus food ordering interactive menu)</td>
        </tr>
        <tr>
          <td><code>http://&lt;public-ip&gt;/</code></td>
          <td><code>/var/www/html/index.html</code></td>
          <td><span class="badge badge-success">200 OK</span></td>
          <td>Multi-Hosting Portal Landing Hub (Navigation links to both sites)</td>
        </tr>
      </tbody>
    </table>

    <h3>Cloud Multi-Hosting Engineering Best Practices</h3>
    <ul>
      <li><strong>Security Group Inbound Authorizations:</strong> Always ensure Port 80 (HTTP) is explicitly opened to <code>0.0.0.0/0</code> in the AWS Security Group. If missing, requests will timeout at the cloud boundary before reaching the VM.</li>
      <li><strong>Filesystem Permissions:</strong> Apache processes execute under the <code>apache</code> service account. Directories must maintain <code>755</code> permissions so the daemon can traverse subdirectories without throwing <code>403 Forbidden</code> errors.</li>
      <li><strong>Process &amp; Port Verification:</strong> Use <code>sudo ss -tulpn | grep ':80'</code> to verify the Apache daemon is actively bound and listening on the HTTP port.</li>
    </ul>

    <h2>Conclusion</h2>
    <p>
      In this laboratory practical, I systematically explored the architectural foundations of cloud virtualization, analyzing the operational and financial differences between bare-metal physical servers and hypervisor-driven cloud virtual machines. I examined the end-to-end request handling flow of web hosting in cloud infrastructures, including DNS mapping, cloud ingress security group filtering, TCP socket binding, and web server request routing.
    </p>
    <p>
      Furthermore, I studied the three primary multi-hosting strategies &mdash; port-based, name-based, and directory-based virtual hosting. Practically, I launched a single AWS EC2 instance (<code>lab5-web-2</code>, Instance ID: <code>i-0ff8aef326439e30c</code>, <code>t3.micro</code>, Amazon Linux 2023) in the Mumbai <code>ap-south-1b</code> region, configured an Apache web server, and successfully deployed two distinct web applications (<em>Aditya's Portfolio</em> at <code>/site1/</code> and <em>Campus Eats</em> at <code>/site2/</code>) alongside a master landing hub. Both websites were independently verified live from a web browser over standard Port 80, proving how multi-hosting maximizes compute efficiency and lowers cloud infrastructure costs.
    </p>

    <div style="margin-top: 40px; border-top: 1px solid #cbd5e1; padding-top: 18px;">
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

print(f"Successfully generated {html_path} ({len(html)} bytes)!")
