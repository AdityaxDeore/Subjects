# Software Requirements Specification
## Amazon India E-Commerce Platform — v1.0

## 1. Introduction
### 1.1 Purpose
Define the functional, non-functional, security, performance, and operational requirements for the Amazon India E-Commerce Platform. The system supports product discovery, shopping cart management, secure checkout, payments, order management, delivery tracking, customer support, reviews, promotions, and third-party seller operations.
### 1.2 Scope
A web and mobile e-commerce platform connecting customers, third-party sellers, delivery agents, payment providers, and administrators. The scope includes product search and discovery, shopping cart, checkout, multiple payment methods, order tracking, customer accounts, seller management, reviews and ratings, promotions, customer support, and logistics integration.
### 1.3 Intended Audience
Software engineers, database developers, UI/UX designers, QA engineers, testers, product managers, system administrators, and project stakeholders.
### 1.4 Assumptions & Dependencies
Users are assumed to have a stable internet connection and use modern web browsers or supported Android/iOS devices. Payment processing depends on external banking, UPI and payment gateway services, while delivery estimates and tracking depend on external logistics and routing services. The system also depends on cloud infrastructure and third-party APIs.

## 2. User Roles

| Role | Description |
|---|---|
| Shopper / Customer | Browses products, searches and filters items, reads reviews, manages the cart, places orders, makes payments, tracks deliveries, and raises support requests. |
| Seller | Uploads products and inventory, manages pricing, applies promotions, processes customer orders, and uses the seller dashboard. |
| Delivery Agent | Scans packages, follows optimized delivery routes, updates delivery status, and verifies successful delivery using OTP or digital confirmation. |
| Warehouse Staff | Handles product inventory intake, bin allocation, pick-and-pack fulfillment, package labeling, and dispatch to carrier hubs. |
| Administrator | Monitors the platform, manages categories and site configuration, handles major disputes, and oversees overall system operations. |

## 3. Functional Requirements

| # | Category | Requirement | Priority |
|---|---|---|---|
| FR-01 | Product Search | The system shall allow customers to search products using keywords, categories, voice search, filters, typo tolerance, and regional-language synonyms. | High |
| FR-02 | Product Discovery | The system shall allow customers to filter products by price, brand, ratings, and delivery eligibility. | Medium |
| FR-03 | Shopping Cart | The system shall allow customers to add, remove, and modify product quantities in their shopping cart. | High |
| FR-04 | Cart Synchronization | The system shall persist and synchronize shopping cart data across web and mobile sessions. | High |
| FR-05 | Checkout | The system shall provide a multi-step checkout process including address selection, delivery options, payment, and order confirmation. | High |
| FR-06 | Payment | The system shall support UPI, credit/debit cards, net banking, Amazon Pay Wallet, and Cash on Delivery. | High |
| FR-07 | Order Management | The system shall generate a unique order ID for every successful transaction and allow customers to view order history. | High |
| FR-08 | Order Tracking | The system shall display order progress through statuses such as Ordered, Processing, Shipped, Out for Delivery, Delivered, and Returned. | High |
| FR-09 | Order Cancellation | The system shall allow customers to cancel an order before it reaches the shipped stage. | Medium |
| FR-10 | Account Management | The system shall allow customers to manage profile information, multiple delivery addresses, and saved payment methods. | Medium |
| FR-11 | Customer Support | The system shall provide chatbot-based customer support and transfer unresolved issues to a human support agent. | Medium |
| FR-12 | Notifications | The system shall send users notifications when important order or delivery milestones occur. | Medium |

## 4. Non-Functional Requirements

| # | Category | Requirement | Priority |
|---|---|---|---|
| NFR-01 | Performance | Search responses shall normally be returned within 300 milliseconds. | High |
| NFR-02 | Performance | Homepage and initial search results shall render within 2 seconds on standard 4G connections. | High |
| NFR-03 | Scalability | The platform shall support extremely high concurrent transaction volumes during major sales events. | High |
| NFR-04 | Security | Passwords shall be securely salted and hashed using a modern password-hashing algorithm such as Argon2. | High |
| NFR-05 | Payment Security | Raw CVV data shall never be stored or logged, and saved card information shall be tokenized. | High |
| NFR-06 | Reliability | The platform shall target 99.999% availability using highly available infrastructure. | High |
| NFR-07 | Disaster Recovery | Core databases shall be backed up at regular intervals and the disaster recovery process shall target less than 30 minutes of maximum tolerable downtime. | Medium |
| NFR-08 | Data Protection | Critical user and payment-related information shall comply with applicable Indian data protection and localization requirements. | High |
| NFR-09 | Accessibility / Usability | The interface shall remain responsive across desktop, tablet, and smartphone screen sizes. | Medium |

## 5. Use Cases

### UC-1: Search and Browse Products
- **Actor:** Shopper / Customer
- **Flow:** 1. Enter product name or keyword. 2. View search results. 3. Apply filters (price, brand, rating). 4. Select a product.

### UC-2: Purchase Product
- **Actor:** Shopper / Customer
- **Flow:** 1. Add product to cart. 2. Proceed to checkout. 3. Select address and delivery option. 4. Make payment. 5. Confirm order.

### UC-3: Track Order
- **Actor:** Shopper / Customer
- **Flow:** 1. Open Your Orders. 2. Select an order. 3. Click Track Package. 4. View delivery status.

### UC-4: Manage Account
- **Actor:** Shopper / Customer
- **Flow:** 1. Open Account Settings. 2. Add or edit address. 3. Verify PIN code. 4. Save changes.

### UC-5: Review Product
- **Actor:** Shopper / Customer
- **Flow:** 1. Open purchased product. 2. Select Write a Review. 3. Give rating and feedback. 4. Submit review.

### UC-6: Manage Product Listings
- **Actor:** Seller
- **Flow:** 1. Open Seller Dashboard. 2. Add or edit product listings. 3. Update inventory and price. 4. Manage active promotions.

### UC-7: Manage Products & Orders
- **Actor:** Seller
- **Flow:** 1. Open Seller Dashboard. 2. View new customer orders. 3. Verify stock availability. 4. Process order packaging. 5. Hand over to logistics.

### UC-8: Manage Deliveries
- **Actor:** Delivery Agent
- **Flow:** 1. View assigned deliveries on mobile app. 2. Scan the package barcode. 3. Follow optimized delivery route. 4. Update transit status. 5. Request delivery OTP from customer.

### UC-9: Deliver Order
- **Actor:** Delivery Agent
- **Flow:** 1. View assigned order. 2. Scan the package. 3. Follow the delivery route. 4. Update delivery status. 5. Verify delivery using OTP. 6. Mark order as delivered.

### UC-10: Manage Platform
- **Actor:** Admin
- **Flow:** 1. Open Admin Dashboard. 2. Monitor platform activity. 3. Manage product categories and site settings. 4. Handle major customer-seller disputes. 5. Update platform configurations.

### UC-11: Manage Inventory & Shipments
- **Actor:** Warehouse Staff
- **Flow:** 1. View pending orders. 2. Check product availability. 3. Pick and pack products. 4. Update inventory. 5. Generate shipping details. 6. Mark package as dispatched.
