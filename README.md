# Real Estate Management 🏠

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple?style=for-the-badge&logo=odoo)
![License](https://img.shields.io/badge/License-LGPL%203-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Development-orange?style=for-the-badge)

A comprehensive Odoo project containing modules for managing real estate properties and card reader systems. This repository serves as a development playground for Odoo best practices, adhering to Odoo 18.0 guidelines.

## 🚀 Modules

| Directory | Module Name | Description | Status |
| :--- | :--- | :--- | :--- |
| **`estate`** | **Real Estate** | Full-featured property management system with offers, tagging, and workflow automation. | 🚧 In Progress |
| **`carddd`** | **Card Reader System** | System for managing physical card data, reading logs, and reader device integration. | 🚧 In Progress |

## ✨ Features

### 🏡 Estate Module

- **Property Tracking**: Detailed records for properties including price, bedrooms, living area, garden, and availability.
- **Offer Management**: Handle property offers from potential buyers with acceptance/refusal workflows.
- **Smart Categorization**: Organize properties using hierarchical Types (e.g., House, Apartment) and flexible Tags.
- **Process Workflow**: State machine implementation for property lifecycle (New → Offer Received → Offer Accepted → Sold/Canceled).
- **Calculated Fields**: Automatic computation of total areas and best offer prices.

### 💳 Card Reader Module (carddd)

- **Card Management**: Store and manage physical card UIDs.
- **Activity Logging**: Track every card reading event.
- **Device Integration**: Structure for API integration with card reader hardware.

## 🛠 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rasyaakbar-dev/Real-Estate.git
   ```

2. **Add to Odoo Addons Path**:
   Add the parent directory of this repository to your `odoo.conf`.
   *Example:*

   ```ini
   addons_path = /path/to/odoo/addons,/your/local/path/to/Real-Estate
   ```

3. **Install in Odoo**:
   - Enable **Developer Mode** in Odoo.
   - Go to **Apps** -> **Update Apps List**.
   - Search for "Real Estate" or "Card Reader".
   - Click **Activate**.

## 📂 Directory Structure

```plaintext
/
├── carddd/             # Card Reader System module
│   ├── models/         # Card logic
│   ├── views/          # Card management views
│   ├── demo/           # Demo data
│   └── ...
├── estate/             # Main Real Estate module
│   ├── controllers/    # Web controllers
│   ├── models/         # Database models (Property, Offer, etc.)
│   ├── views/          # XML Views (Actions, Menus, Form/Tree views)
│   ├── security/       # Access rights (IR Model Access)
│   ├── demo/           # Demo data
│   ├── __init__.py     # Python package marker
│   └── __manifest__.py # Module metadata
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the LGPL-3 License. See `LICENSE.txt` for more information.
