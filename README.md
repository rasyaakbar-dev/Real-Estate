# Real Estate Management 🏠

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple?style=for-the-badge&logo=odoo)
![License](https://img.shields.io/badge/License-LGPL-3-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Development-orange?style=for-the-badge)

A comprehensive Odoo module for managing real estate properties. This project is a personal playground for exploring Odoo development best practices, featuring a `card` demo module and the core `estate` management system.

## 🚀 Modules

| Module | Description | Status |
| :--- | :--- | :--- |
| **`estate`** | Core real estate management: Property listings, Offers, Types, and Tags. | 🚧 In Progress |
| **`card`** | Simple card/demo module for testing basic views and models. | 🚧 In Progress |

## ✨ Features (Estate)

- **Property Management**: Track property details (Price, Bedrooms, Living Area, Garden).
- **Offers System**: Manage offers from potential buyers.
- **Categorization**: Organize properties by Type (House, Apartment) and Tags.
- **Workflow**: State machine for property status (New, Offer Received, Sold, Canceled).

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rasyaakbar-dev/Real-Estate.git
   ```

2. **Add to Odoo Addons Path**:
   Add the parent directory of this repository to your `odoo.conf`:
   ```ini
   addons_path = /path/to/odoo/addons,/path/to/Real-Estate
   ```

3. **Install**:
   - Update your Odoo Apps list.
   - Search for "Real Estate".
   - Click **Install**.

## 📂 Directory Structure

```plaintext
/
├── card/               # Demo module
├── estate/             # Main Real Estate module
│   ├── models/         # Database models (Python)
│   ├── views/          # XML Views & Actions
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