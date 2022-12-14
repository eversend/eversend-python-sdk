# Eversend Python SDK

[![PyPI version](https://badge.fury.io/py/eversend.svg)](https://badge.fury.io/py/eversend) [![Build Status][travis-image]][travis-url] ![Dependencies](https://img.shields.io/librariesio/release/pypi/eversend)

Python SDK for Eversend payments API

## Table of Contents

1. [Installation](#installation)
2. [Initialization](#initialization)
3. [Usage](#usage)
4. [Contribution Guidelines](#contribution-guidelines)
5. [License](#license)
## Installation

```sh
$ pip install -U eversend
```

## Initialization

```python
from eversend import Eversend

eversendClient = Eversend(clientId= 'clientId', clientSecret= 'clientSecret', version='v1')

wallets = eversendClient.Wallets.list();
```

You can get your clientId and clientSecret from the settings section in the [dashboard](https://business.eversend.co/settings)

## Usage
### Wallets

**Get all wallets**

```python
wallets = eversendClient.Wallets.list();
```

**Get one wallet**

```python
wallets = eversendClient.Wallets.getOne('USD');
```
### Transactions

**Get all transactions**

```python
transactions = eversendClient.Transactions.list(
    page = 1,
    limit = 10
);
```

If `page` and `limit` are not set, the default of `1` and `10` are used respectively.

**Get one transaction**

```python
transaction = eversendClient.Transactions.getOne(
    transactionId= "EVS12345678"
);
```

### Exchange

To exchange from one wallet to another, you first have to generate a quotation. This returns a token with a 30s timeout that you can use to make the exchange.

**Get exchange quotation**

```python
quotation = eversendClient.Exchange.getQuotation(
    source = "USD",
    destination = "UGX",
    amount = 10.0
);
```

**Exchange currency**

```python
exchange = eversendClient.Exchange.exchange(
    token = "dhhsggajjshhdhdhd",
    transactionRef = "EVS-12345678", # optional field
);
```

### Beneficiaries

**Get beneficiaries**

```python
beneficiaries = eversendClient.Beneficiaries.list(
    page = 1,
    limit = 10
);
```

If `page` and `limit` are not set, the default of `1` and `10` are used respectively.

**Get single beneficiary**

```python
beneficiary = eversendClient.Beneficiaries.getOne(
    beneficiaryId = 100
);
```

**Create a beneficiary**

```python
beneficiary = eversendClient.Beneficiaries.create(
    firstName = "John",
    lastName = "Okello",
    country = "UG", # Alpha-2 country code
    phoneNumber = "+256712345678", # Should be in international format
    bankAccountName = "John Okello",
    bankAccountNumber = "12345678",
    bankName = "Stanbic Bank",
    bankCode = 1234 # You can get the bank code from payouts.getDeliveryBanks()
);
```
>Note that all bank fields are optional if bank payments will not be required

**Edit a beneficiary**

```python
beneficiary = eversendClient.Beneficiaries.update(
    beneficiaryId = 100,
    firstName = "John",
    lastName = "Okello",
    country = "UG", # Alpha-2 country code
    phoneNumber = "+256712345678", # Should be in international format
    bankAccountName = "John Okello",
    bankAccountNumber = "12345678",
    bankName = "Stanbic Bank",
    bankCode = 1234 # You can get the bank code from payouts.getDeliveryBanks()
);
```
>Note that all bank fields are optional if bank payments will not be required

**Delete a beneficiary**

```python
eversendClient.Beneficiaries.delete(
    beneficiaryId = 100
);
```

### Collections

**Get collection fees**

```python
collectionFees = eversendClient.Collections.getFees(
    amount = 1000,
    currency = "KES",
    method = "momo"
);
```

**Get collection OTP**

>Required when initiating mobile money collections
```python
collectionOTP = eversendClient.Collections.getOTP(
    phone = "+256712345678"
);
```

**Initiate Mobile Money collection**

```python
collection = eversendClient.Collections.initiate(
    method = "momo",
    phone = "+256712345678",
    amount = 1000,
    country = "UG",
    currency = "UGX",
    pin = 123456, # From phone number passed in Get Collection OTP
    pinId = "dg524fhsgfde", # From Get Collection OTP
    transactionRef = "EVS-12345678", # Optional transaction ref generated by you
    customer = { name = "John Okello" } # Optional customer object with your metadata
);
```
### Payouts

**Get payout quotation**

```python
quotation = eversendClient.Payouts.getQuotation(
    sourceWallet = "USD",
    amount = 100,
    type = "momo",
    destinationCountry = "KE",
    destinationCurrency = "KES",
    amountType = "SOURCE", # amountType can be SOURCE or DESTINATION
);
```
>`amountType` refers to whether you want amount to represent `sourceWallet` (SOURCE) or `destinationCurrency` (DESTINATION)

**Pay existing beneficiary**

```python
payout = eversendClient.Payouts.initiate(
    beneficiaryId = 100,
    quotationToken = "token",
    transactionRef = "EVS-12345678" # Optional transaction ref generated by you
);
```

**Pay new beneficiary**

```python
payout = eversendClient.Payouts.initiate(
    firstName = "John",
    lastName = "Okello",
    country = "UG", # Alpha-2 country code
    phoneNumber = "+256712345678", # Should be in international format
    bankAccountName = "John Okello",
    bankAccountNumber = "12345678",
    bankName = "Stanbic Bank",
    bankCode = 1234, # You can get the bank code from payouts.getDeliveryBanks()
    quotationToken = "token",
    transactionRef = "EVS-12345678" # Optional transaction ref generated by you
);
```

**Get delivery countries**

```python
countries = eversendClient.Payouts.countries()
```

**Get delivery banks**

```python
banks = eversendClient.Payouts.banks(
    country = "UG"
);
```
## Contribution Guidelines

Contributions are welcome and encouraged. Learn more about our contribution guidelines [here](/CONTRIBUTING.md)
## License

MIT ?? [Eversend]()

[pypi-image]: https://badge.fury.io/py/eversend.svg
[npm-url]: https://badge.fury.io/js/@eversend%2Fnode-sdk
[travis-image]: https://app.travis-ci.com/eversend/eversend-python-sdk.svg?token=WxxstsCyyxGyzLpHFkUi&branch=master
[travis-url]: https://app.travis-ci.com/eversend/eversend-python-sdk
