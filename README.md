# Real Estate Management

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple?style=flat-square&logo=odoo)
![License](https://img.shields.io/badge/License-LGPL--3-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Development-orange?style=flat-square)

A comprehensive Odoo project for managing real estate properties and card reader systems.

## Table of Contents

- [Description](#description)
- [Modules](#modules)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Description

This repository contains Odoo 18.0 modules designed for property management businesses. It provides tools for tracking properties, managing offers, and integrating card reader hardware.

### Business Use Case

Real estate agencies can use this system to:

- Track property listings with detailed attributes
- Manage buyer offers with acceptance/refusal workflows
- Categorize properties using types and tags
- Monitor property lifecycle from listing to sale

## Modules

| Module          | Technical Name | Summary                                                        |
|-----------------|----------------|----------------------------------------------------------------|
| **Real Estate** | `estate`       | Property management with offers, tags, and workflow automation |
| **Card Reader** | `carddd`       | Card UID management and reading activity logs                  |

See individual module `readme/` directories for detailed documentation.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/rasyaakbar-dev/Real-Estate.git
   ```

2. **Add to Odoo addons path** in `odoo.conf`:

   ```ini
   addons_path = /path/to/odoo/addons,/path/to/Real-Estate
   ```

3. **Install modules**
   - Enable Developer Mode in Odoo
   - Go to **Apps** → **Update Apps List**
   - Search for "Real Estate" or "Card Reader"
   - Click **Activate**

## Configuration

After installation:

1. Go to **Real Estate** menu
2. Configure **Property Types** (House, Apartment, etc.)
3. Create **Property Tags** for categorization

## Usage

### Property Management

1. Create a new property with details (bedrooms, living area, price)
2. Receive and manage offers from potential buyers
3. Accept or refuse offers to progress property state
4. Mark properties as Sold or Canceled

### Card Reader

1. Register cards with their UIDs
2. View reading activity logs

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## Credits

### Authors

- Rasya A.N
- Thanzero07

### Contributors

- Rasya A.N - Initial development
- Thanzero07 - Card module development

## License

Distributed under the **LGPL-3** License. See [LICENSE.txt](LICENSE.txt) for details.
