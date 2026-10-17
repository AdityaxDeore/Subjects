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

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloud Computing Lab 4 - Cloud Networking (VPC &amp; Load Balancing)</title>

<!-- Mermaid for Architecture Diagrams -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({{ 
      startOnLoad: true, 
      theme: 'neutral',
      flowchart: {{ curve: 'basis', htmlLabels: true }}
  }});
</script>

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

  @media print {{
    body {{
      background: #ffffff;
      padding: 0;
    }}
    .container {{
      max-width: 100%;
      margin: 0;
      box-shadow: none;
    }}
    .page {{
      width: 100%;
      min-height: auto;
      margin: 0;
      padding: 0.45in 0.5in;
      box-shadow: none;
      border: none;
      page-break-after: always;
      border-radius: 0;
    }}
    .page:last-child {{
      page-break-after: avoid;
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

  /* Typography (Exact IAM UI) */
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

  /* Styled Tables (Exact IAM UI) */
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

  /* Info Callouts (Exact IAM UI) */
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

  /* Free Pasted Images (Big, natural, zero boxes, zero canvas, zero borders) */
  .free-img {{
    margin: 22px 0 10px 0;
    text-align: center;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
  }}
  .free-img img {{
    width: 100%;
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    background: transparent !important;
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
  .caption strong {{
    color: #0f172a;
    font-style: normal;
  }}

  .badge {{
    display: inline-block;
    padding: 3px 8px;
    border-radius: 5px;
    font-size: 7.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    vertical-align: middle;
    margin-left: 8px;
  }}
  .badge.blue {{ background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }}
  .badge.green {{ background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }}
  .badge.purple {{ background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }}

  /* Diagram Box */
  .diagram-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 18px;
    margin: 18px 0;
    text-align: center;
  }}
</style>
</head>
<body>
<div class="container" contenteditable="true">

  <!-- ==========================================================================
       PAGE 1: Cover Header, Title, Aim, Objectives
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
          Assignment No. 4
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left">
          Course:- Cloud Computing
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left">
          Name:- Aditya Chandrajit Deore
        </td>
      </tr>
      <tr>
        <td colspan="2" class="row-left">
          PRN:- 124B1F116 &nbsp;&nbsp;|&nbsp;&nbsp; Batch:- B3
        </td>
      </tr>
    </table>

    <h2>TITLE</h2>
    <p><strong>Lab 4: Cloud Networking (VPC &amp; Load Balancing)</strong></p>

    <h2>AIM</h2>
    <p>
      To design, configure, and evaluate a custom Virtual Private Cloud (VPC) / Virtual Cloud Network (VCN) featuring public and private subnets, establish bidirectional and secure outbound internet connectivity using an Internet Gateway and route tables, launch two virtual machine compute instances distributed across multiple Availability Zones / Fault Domains, and implement an Application Load Balancer (ALB) with automated health checks to distribute incoming HTTP traffic and achieve high availability.
    </p>

    <h2>OBJECTIVES</h2>
    <ul>
      <li>To understand the architectural design principles of software-defined cloud networking, including VPC/VCN isolation, CIDR prefix allocation, and route table mechanics.</li>
      <li>To analyze the functional, routing, and security differences between public and private subnets.</li>
      <li>To configure virtual networking components: Internet Gateway (IGW), Network Address Translation (NAT) Gateway, and route tables adhering to the Longest Prefix Match (LPM) algorithm.</li>
      <li>To implement multi-layered defense-in-depth security using stateful Security Groups / Network Security Groups (NSGs) and stateless Network ACLs / Security Lists.</li>
      <li>To deploy two web server virtual machine instances (EC2 / OCI Compute) across distinct physical Availability Zones (<code>ap-south-1a</code> and <code>ap-south-1b</code>).</li>
      <li>To provision an Application Load Balancer (ALB) with target group listeners and HTTP health checks.</li>
      <li>To verify end-to-end traffic distribution, round-robin load balancing, and fault tolerance via real-time browser inspection.</li>
    </ul>

    <div class="info-box blue">
      <strong>Enterprise Environment Summary:</strong> Primary Cloud Platform: Amazon Web Services (AWS) in Region <code>ap-south-1 (Mumbai)</code> | Custom VPC: <code>aditya-vpc-vpc</code> (<code>10.0.0.0/16</code>) | Comparative Architecture: Oracle Cloud Infrastructure (OCI Always Free VCN).
    </div>
  </div>

  <!-- ==========================================================================
       PAGE 2: High-Level Architecture & Traffic Flowchart
       ========================================================================== -->
  <div class="page">
    <h2>SYSTEM ARCHITECTURE &amp; CLOUD NETWORKING FLOWCHART</h2>
    
    <p>
      Modern enterprise cloud architectures rely on tiered network topologies that separate public-facing entry points from private computing resources. The diagram below illustrates the end-to-end data path, from external internet clients through the AWS Internet Gateway and Application Load Balancer to the backend compute servers running across distinct Availability Zones.
    </p>

    <div class="diagram-box">
      <div class="mermaid">
      flowchart TD
          Client["Client Web Browser (Internet Requestor)"] -->|HTTP Port 80| IGW["AWS Internet Gateway (igw-0a561d52ed88ee322)"]
          subgraph VPC ["Custom VPC: aditya-vpc-vpc (10.0.0.0/16) in ap-south-1 (Mumbai)"]
              IGW --> RT["Public Route Table (rtb-03c715a137972aa3d)<br/>Rule: 0.0.0.0/0 &rarr; Target: igw-0a561d52ed88ee322"]
              RT --> ALB["Application Load Balancer: aditya-web-alb<br/>Security Group: aditya-alb-sg (Port 80 Allowed)"]
              ALB --> TG["Target Group: aditya-web-tg (HTTP:80 | Health Checks: /)"]
              subgraph AZ1 ["Availability Zone: ap-south-1a"]
                  TG -->|Traffic Distribution 50%| VM1["EC2: aditya-web-1 (t3.micro)<br/>Subnet: public1-ap-south-1a<br/>Web Page: Server 1 (ap-south-1a)"]
              end
              subgraph AZ2 ["Availability Zone: ap-south-1b"]
                  TG -->|Traffic Distribution 50%| VM2["EC2: aditya-web-2 (t3.micro)<br/>Subnet: public2-ap-south-1b<br/>Web Page: Server 2 (ap-south-1b)"]
              end
          end
      </div>
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
        <strong>Multi-Tenant Isolation:</strong><br>
        Guarantees complete cryptographic and logical isolation between tenants sharing the same physical hyperscaler hardware. Network packets cannot leak across VPC boundaries without explicit peering configurations.
      </li>
      <li>
        <strong>Granular Architectural Control:</strong><br>
        Network engineers define custom private IP address ranges (IPv4/IPv6 CIDR blocks), subnet segmentations, route tables, network gateways, and stateful firewalls.
      </li>
      <li>
        <strong>Defense-in-Depth Security:</strong><br>
        Enables multi-tier network topologies that cleanly separate public-facing ingress resources (load balancers, reverse proxies) from private operational tiers (application servers, relational databases).
      </li>
      <li>
        <strong>Hybrid Cloud Connectivity:</strong><br>
        Seamlessly extends existing enterprise data centers into the cloud via IPSec Virtual Private Network (VPN) tunnels or dedicated private physical links (AWS Direct Connect / OCI FastConnect).
      </li>
      <li>
        <strong>Regulatory Compliance:</strong><br>
        Essential for satisfying strict cybersecurity benchmarks (ISO 27001, SOC 2, PCI-DSS, HIPAA) requiring boundary segmentation of sensitive data workloads.
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
        <strong>CIDR Block (Classless Inter-Domain Routing):</strong><br>
        The contiguous master private IP address space allocated to the VPC (e.g., <code>10.0.0.0/16</code>), defining the maximum address capacity for all resources.
      </li>
      <li>
        <strong>Subnets:</strong><br>
        Logical subdivisions of the VPC CIDR block bound to specific physical Availability Zones (AZs) or regional scopes, creating distinct broadcast domains.
      </li>
      <li>
        <strong>Route Tables:</strong><br>
        Sets of routing rules (destination CIDR &rarr; target gateway) determining the network path traversed by outgoing packets from associated subnets.
      </li>
      <li>
        <strong>Internet Gateway (IGW):</strong><br>
        A redundant, horizontally scaled software gateway facilitating bidirectional communication between public subnet instances and the public internet.
      </li>
      <li>
        <strong>NAT Gateway / NAT Instance:</strong><br>
        A managed network translation service enabling private subnet instances to initiate outbound requests to the internet without allowing external internet clients to initiate inbound connections.
      </li>
      <li>
        <strong>Virtual Firewalls (Security Groups &amp; NACLs / Security Lists):</strong><br>
        Stateful instance-level (Security Groups / NSGs) and stateless subnet-level (NACLs / Security Lists) packet filtering engines controlling traffic flows.
      </li>
      <li>
        <strong>Load Balancers (ALB / NLB):</strong><br>
        Intelligent reverse proxies distributing client traffic across healthy backend compute targets across multiple availability zones.
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
        <strong>Default Routing Target:</strong><br>
        It provides a destination target in the VPC route tables for internet-bound traffic via the default route <code>0.0.0.0/0</code>.
      </li>
      <li>
        <strong>1:1 Network Address Translation (NAT):</strong><br>
        When an instance in a public subnet initiates an outbound connection, the IGW translates its private IPv4 address to its associated public IPv4 address. Conversely, for incoming traffic addressed to the instance's public IP, the IGW translates the destination public IP back into the instance's private IP before forwarding the packet into the VPC software-defined network overlay.
      </li>
    </ul>

    <h3>5. How Does Network Isolation Improve Security in a Cloud Environment?</h3>
    <p>
      Network isolation applies the <strong>Principle of Least Privilege (PoLP)</strong> and <strong>Zero Trust Architecture</strong> to network topologies through four defensive mechanisms:
    </p>

    <ul>
      <li>
        <strong>Attack Surface Reduction:</strong><br>
        By placing database servers, payment engines, and backend APIs in private subnets with no public IPs, external attackers cannot directly scan, ping, or exploit them over the public internet.
      </li>
      <li>
        <strong>Blast Radius Containment:</strong><br>
        If a public-facing web server or reverse proxy is compromised through a web application vulnerability, the attacker cannot freely pivot through the network; access to backend subnets is strictly policed by internal firewall rules.
      </li>
      <li>
        <strong>Defense-in-Depth:</strong><br>
        Multiple complementary layers of protection (perimeter IGW &rarr; Subnet NACL / Security List &rarr; Instance Security Group &rarr; Host OS Firewall) ensure that the failure of any single security control does not expose core assets.
      </li>
      <li>
        <strong>Compliance Enforcement:</strong><br>
        Regulatory standards (PCI-DSS Section 1.3, HIPAA Security Rule) mandate that cardholder data and protected health information (PHI) reside in network zones completely segregated from untrusted external networks.
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
    
    <p style="text-align: center; margin: 14px 0;">$$\\text{{IPv4 Address}} / \\text{{Prefix Length (bits)}}$$</p>
    
    <p>
      The total number of IP addresses available in a given prefix block is determined mathematically by the formula:
    </p>
    <p style="text-align: center; margin: 14px 0;">$$\\text{{Total Addresses}} = 2^{{(32 - \\text{{Prefix Length}})}}$$</p>

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
        <strong>AWS reserves 5 IP addresses per subnet:</strong><br>
        <code>.0</code> (Network), <code>.1</code> (VPC Router), <code>.2</code> (DNS Server - AmazonProvidedDNS), <code>.3</code> (Future use), and <code>.255</code> (Network broadcast).
      </li>
      <li>
        <strong>Oracle Cloud (OCI) reserves 3 IP addresses per subnet:</strong><br>
        <code>.0</code> (Network), <code>.1</code> (Default Gateway), and <code>.2</code> (Reserved by OCI).
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
        <strong>Longest Prefix Match (LPM) Evaluation:</strong><br>
        When routing an outgoing packet, the virtual router evaluates all destination CIDR rules in the route table and selects the most specific match (the one with the largest prefix length / most specific bitmask).<br>
        For instance, if a packet is addressed to <code>10.0.0.15</code>:
        <ul style="margin-top: 6px; margin-bottom: 6px;">
          <li>Rule 1: <code>10.0.0.0/16 &rarr; local</code> (Prefix length 16)</li>
          <li>Rule 2: <code>0.0.0.0/0 &rarr; igw-xxxxxxxxx</code> (Prefix length 0)</li>
        </ul>
        The router matches Rule 1 because <code>/16</code> is longer and more specific than <code>/0</code>, keeping local traffic securely inside the VPC without sending it to the Internet Gateway.
      </li>
      <li>
        <strong>Default Quad-Zero Route (<code>0.0.0.0/0</code>):</strong><br>
        Acts as the catch-all default gateway for any destination address that does not match a more specific local or peered CIDR.
        <ul style="margin-top: 6px; margin-bottom: 6px;">
          <li>In a <strong>Public Subnet</strong>, <code>0.0.0.0/0 &rarr; Target: Internet Gateway</code>.</li>
          <li>In a <strong>Private Subnet</strong>, <code>0.0.0.0/0 &rarr; Target: NAT Gateway</code>.</li>
        </ul>
      </li>
      <li>
        <strong>Subnet Associations:</strong><br>
        Every subnet in a VPC must be explicitly or implicitly associated with a route table. Multiple subnets can share a single route table, but a subnet can only be associated with one route table at a time.
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
        <strong>Sign in to OCI Console:</strong><br>
        Access <code>cloud.oracle.com</code> and select your assigned home region (e.g., <code>ap-mumbai-1</code> or <code>ap-hyderabad-1</code>).
      </li>
      <li>
        <strong>Open Networking Navigation:</strong><br>
        Expand the navigation burger menu &rarr; <strong>Networking</strong> &rarr; <strong>Virtual Cloud Networks</strong>.
      </li>
      <li>
        <strong>Launch VCN Wizard:</strong><br>
        Click the <strong>Start VCN Wizard</strong> button. Select <strong>Create VCN with Internet Connectivity</strong> &rarr; click <strong>Start VCN Wizard</strong>.
      </li>
      <li>
        <strong>Define VCN Parameters:</strong><br>
        Enter the network parameters in the wizard:
        <ul style="margin-top: 6px; margin-bottom: 6px;">
          <li><strong>VCN Name:</strong> <code>aditya-pccoe-vcn</code></li>
          <li><strong>Compartment:</strong> Select your root or designated laboratory compartment.</li>
          <li><strong>VCN IPv4 CIDR Block:</strong> <code>10.0.0.0/16</code></li>
          <li><strong>Public Subnet IPv4 CIDR Block:</strong> <code>10.0.0.0/24</code></li>
          <li><strong>Private Subnet IPv4 CIDR Block:</strong> <code>10.0.1.0/24</code></li>
        </ul>
      </li>
      <li>
        <strong>Review Automated Architecture:</strong><br>
        The wizard automatically provisions:
        <ul style="margin-top: 6px; margin-bottom: 6px;">
          <li>1 Internet Gateway (<code>IGW</code>) for public internet communication.</li>
          <li>1 NAT Gateway (<code>NATGW</code>) for private outbound updates.</li>
          <li>1 Service Gateway (<code>SGW</code>) for private access to Oracle Object Storage and APIs.</li>
          <li>Default Route Tables and Default Security Lists with SSH/HTTP ingress rules.</li>
        </ul>
      </li>
      <li>
        <strong>Create VCN:</strong><br>
        Click <strong>Create</strong>. OCI orchestrates and validates all resources in under 15 seconds.
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
        <strong>VPC CIDR Master Block:</strong><br>
        <code>10.0.0.0/16</code> (65,536 total addresses) in Region <code>ap-south-1</code> (Mumbai).
      </li>
      <li>
        <strong>Public Subnet 1 (<code>aditya-vpc-subnet-public1-ap-south-1a</code>):</strong><br>
        &bull; CIDR Block: <code>10.0.0.0/20</code> (4,096 IP addresses) | Availability Zone: <code>ap-south-1a</code><br>
        &bull; Route Table: <code>rtb-03c715a137972aa3d</code> with route <code>0.0.0.0/0 &rarr; igw-0a561d52ed88ee322</code><br>
        &bull; Auto-assign Public IPv4: <strong>Enabled</strong>
      </li>
      <li>
        <strong>Public Subnet 2 (<code>aditya-vpc-subnet-public2-ap-south-1b</code>):</strong><br>
        &bull; CIDR Block: <code>10.0.16.0/20</code> (4,096 IP addresses) | Availability Zone: <code>ap-south-1b</code><br>
        &bull; Route Table: <code>rtb-03c715a137972aa3d</code> with route <code>0.0.0.0/0 &rarr; igw-0a561d52ed88ee322</code><br>
        &bull; Auto-assign Public IPv4: <strong>Enabled</strong>
      </li>
      <li>
        <strong>Private Subnets (Architecture Equivalent):</strong><br>
        &bull; Subnet CIDR: <code>10.0.128.0/20</code> and <code>10.0.144.0/20</code><br>
        &bull; Route Table: Local VPC route only (<code>10.0.0.0/16 &rarr; local</code>) or routed via NAT Gateway.<br>
        &bull; Auto-assign Public IPv4: <strong>Disabled</strong>
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
          <td><code>x.x.x.x/32</code> (Admin IP)</td>
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
      <li><strong>Instance 1:</strong> <code>aditya-web-1</code> (ID: <code>i-0a5792d92f3def505</code>) deployed in <code>public1-ap-south-1a</code>.</li>
      <li><strong>Instance 2:</strong> <code>aditya-web-2</code> (ID: <code>i-076bf7e774cb90044</code>) deployed in <code>public2-ap-south-1b</code>.</li>
      <li><strong>Hardware Profile:</strong> AWS <code>t3.micro</code> (1 vCPU, 1 GB RAM, 20 GB gp3 storage) / OCI <code>VM.Standard.E2.1.Micro</code> Always Free.</li>
    </ul>

    <h4>Automated Bootstrap via User Data (Cloud-Init)</h4>
    <p>
      During instance launch, the following shell script was injected to initialize Apache and generate dynamic, server-identifying web pages:
    </p>

    <pre><code>#!/bin/bash
# Update repository package indices and install Apache web server
apt-get update -y && apt-get install -y apache2

# Enable and start the Apache service
systemctl start apache2
systemctl enable apache2

# Query AWS instance metadata service (IMDSv2 / IMDSv1)
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id || hostname)
AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone || echo "AZ-Cluster")
PRIVATE_IP=$(curl -s http://169.254.169.254/latest/meta-data/local-ipv4 || hostname -I)

# Deploy diagnostic HTML response
cat &lt;&lt;EOF &gt; /var/www/html/index.html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;PCCOE Cloud Lab 4 - Web Server&lt;/title&gt;
&lt;/head&gt;
&lt;body style="text-align:center; padding-top:40px; font-family:sans-serif;"&gt;
  &lt;h1&gt;PCCOE Cloud Lab 4 &mdash; Traffic Routed Successfully&lt;/h1&gt;
  &lt;p&gt;&lt;strong&gt;Instance ID:&lt;/strong&gt; $INSTANCE_ID&lt;/p&gt;
  &lt;p&gt;&lt;strong&gt;Availability Zone:&lt;/strong&gt; $AZ&lt;/p&gt;
  &lt;p&gt;&lt;strong&gt;Private IP:&lt;/strong&gt; $PRIVATE_IP&lt;/p&gt;
  &lt;p&gt;Student: Aditya Chandrajit Deore (PRN: 124B1F116)&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
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
        <strong>Managed NAT Gateway (Network Address Translation):</strong><br>
        Deployed in a <strong>public subnet</strong> and assigned a static Elastic Public IP. The route table associated with the private subnet specifies a default route:
        <p style="text-align: center; margin: 10px 0;">$$\\text{{Destination: }} 0.0.0.0/0 \\implies \\text{{Target: }} \\text{{nat-xxxxxxxxx}}$$</p>
        The NAT Gateway translates outbound TCP/UDP requests to its Elastic IP and forwards them to the Internet Gateway. Inbound connection attempts from external internet hosts to the NAT Gateway are automatically rejected.
      </li>
      <li>
        <strong>VPC Endpoints &amp; PrivateLink (or OCI Service Gateway):</strong><br>
        Allows private instances to access native cloud provider storage and database services (AWS S3, DynamoDB, OCI Object Storage) through a private network interface inside the VPC without traversing the internet or needing a NAT Gateway.
      </li>
      <li>
        <strong>Bastion Host / SSH Jump Server (or Systems Manager / OCI Bastion):</strong><br>
        For administrative access into private instances, administrators connect to an ephemeral, hardened Bastion host in the public subnet, or utilize AWS SSM Session Manager / OCI Bastion Service, which initiates an outbound TLS tunnel without opening inbound port 22.
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

    <table class="styled-table">
      <thead>
        <tr>
          <th>Configuration Parameter</th>
          <th>Configured Value</th>
          <th>Architectural Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>VPC Name Tag</strong></td>
          <td><code>aditya-vpc-vpc</code></td>
          <td>Identifies the software-defined network boundary.</td>
        </tr>
        <tr>
          <td><strong>IPv4 CIDR Block</strong></td>
          <td><code>10.0.0.0/16</code> (65,536 IPs)</td>
          <td>Provides scalable private address capacity.</td>
        </tr>
        <tr>
          <td><strong>Availability Zones</strong></td>
          <td><code>2</code> (<code>ap-south-1a</code>, <code>ap-south-1b</code>)</td>
          <td>Guarantees multi-datacenter physical fault tolerance.</td>
        </tr>
        <tr>
          <td><strong>Public Subnets</strong></td>
          <td><code>2</code> (<code>10.0.0.0/20</code>, <code>10.0.16.0/20</code>)</td>
          <td>Hosts load balancer nodes and web compute instances.</td>
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

    <table class="styled-table">
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
          <td><strong>Public Subnet 1</strong></td>
          <td><code>subnet-0ebd6b35d0d43b5ad</code> (ap-south-1a)</td>
          <td>Available (IPv4: 10.0.0.0/20)</td>
        </tr>
        <tr>
          <td><strong>Public Subnet 2</strong></td>
          <td><code>subnet-06490a3f10bf7b76b</code> (ap-south-1b)</td>
          <td>Available (IPv4: 10.0.16.0/20)</td>
        </tr>
        <tr>
          <td><strong>Internet Gateway</strong></td>
          <td><code>igw-0a561d52ed88ee322</code> (aditya-vpc-igw)</td>
          <td>Attached to vpc-06efb944088685c0a</td>
        </tr>
        <tr>
          <td><strong>Route Table</strong></td>
          <td><code>rtb-03c715a137972aa3d</code> (aditya-vpc-rtb-public)</td>
          <td>Associated with 2 Subnets</td>
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

    <table class="styled-table">
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

    <table class="styled-table">
      <thead>
        <tr>
          <th>Health Check Setting</th>
          <th>Configured Value</th>
          <th>Operational Logic</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Health Check Protocol</strong></td>
          <td><code>HTTP</code></td>
          <td>Performs standard HTTP application-layer probe.</td>
        </tr>
        <tr>
          <td><strong>Health Check Path</strong></td>
          <td><code>/</code> (Root document)</td>
          <td>Evaluates web server Apache index response.</td>
        </tr>
        <tr>
          <td><strong>Healthy Threshold</strong></td>
          <td><code>3</code> consecutive successes</td>
          <td>Target marked Healthy after 3 consecutive 200 OKs.</td>
        </tr>
        <tr>
          <td><strong>Interval &amp; Timeout</strong></td>
          <td>Interval: <code>30s</code> | Timeout: <code>5s</code></td>
          <td>Probes every 30 seconds; drops after 5s silence.</td>
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

    <table class="styled-table">
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
          <td>Routes incoming packets to designated target group.</td>
        </tr>
        <tr>
          <td><strong>Target Group Selection</strong></td>
          <td><code>aditya-web-tg</code></td>
          <td>Pool containing our dual-zone web servers.</td>
        </tr>
        <tr>
          <td><strong>Traffic Weight</strong></td>
          <td><code>1 (100%)</code></td>
          <td>Full distribution across healthy targets.</td>
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

    <table class="styled-table">
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
          <td><strong>Scheme</strong></td>
          <td><code>Internet-facing</code></td>
          <td>Publicly accessible over the internet.</td>
        </tr>
        <tr>
          <td><strong>Subnet Mappings</strong></td>
          <td><code>ap-south-1a</code>, <code>ap-south-1b</code></td>
          <td>Distributes load across both Availability Zones.</td>
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

    <table class="styled-table">
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

    <table class="styled-table">
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

    <div class="info-box green">
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

    <div class="info-box blue">
      <strong>Traffic Distribution Analysis:</strong> The ALB dynamically alternates client sessions between backend targets using round-robin scheduling. This guarantees equal compute load distribution across both Availability Zones and ensures zero service interruption.
    </div>

    <div class="free-img">
      <img src="{step10_b64}" alt="Step 10 - Website Live Served by Server 1">
    </div>
    <p class="caption"><strong>Figure 11:</strong> Client browser output confirming traffic distributed to Server 1 (ap-south-1a) via ALB.</p>
  </div>

  <!-- ==========================================================================
       PAGE 26: Comparative Analysis, Operational Takeaways & Conclusion
       ========================================================================== -->
  <div class="page">
    <h2>Results, Verification &amp; Comparative Analysis</h2>

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
          <td>AWS Internet Gateway (<code>igw-xxxx</code>)</td>
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

    <h2>CONCLUSION</h2>
    <p>
      In this laboratory assignment, I comprehensively investigated software-defined cloud networking, IP subnetting calculations using CIDR notation, and resilient load balancing. I explored the operational differences between public and private subnets, analyzed route table evaluation via Longest Prefix Matching, and implemented defense-in-depth access control using chained, stateful security groups.
    </p>
    <p>
      Practically, I successfully deployed an end-to-end, highly available web architecture on Amazon Web Services (AWS) in the <code>ap-south-1</code> (Mumbai) region, alongside an architectural mapping for Oracle Cloud Infrastructure (OCI Always Free tier). I configured a custom VPC (<code>aditya-vpc-vpc</code>), dual-zone public subnets, an Internet Gateway, two bootstrapped web server virtual machines (<code>aditya-web-1</code> and <code>aditya-web-2</code>), and an Application Load Balancer (<code>aditya-web-alb</code>). Live browser testing confirmed automated round-robin traffic distribution and multi-zone fault resilience, providing vital practical skills in modern cloud enterprise networking.
    </p>
  </div>

</div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Generated assignment_4.html successfully matching IAM assignment UI with ZERO boxes!")
