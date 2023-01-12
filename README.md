# namecheap-lego-operator

## Description

Namecheap LEGO operator implements the provider side of the `tls-certificates-interface`
to provide signed certificates from an ACME servers, using LEGO
(https://go-acme.github.io/lego).
It uses the  `acme_client` library to get the certificate from the ACME server.

## Config

### Required configuration properties
```
email: <Account email address>
domain: <Domain to request certificate for>
namecheap-username: <Namecheap API user>
namecheap-api-key: <Namecheap API key>
```

### Optional configuration properties
```
namecheap-http-timeout: <API request timeout in seconds>
namecheap-polling-interval: <Time between DNS propagation checks in seconds>
namecheap-propagation-timeout: <Maximum waiting time for DNS propagation in seconds>
namecheap-ttl: <The TTL of the TXT record used for the DNS challenge>
namecheap-sandbox: <Use Namecheap sandbox API>
```
## Usage

Deploy `namecheap-lego-operator`:

If you wish to change the default configuration, create a YAML configuration file with fields you would like to change:


```yaml
namecheap-lego:
  email: <Account email address>
  domain: <Domain to request certificate for>
  namecheap-username: <Namecheap API user>
  namecheap-api-key: <Namecheap API key>
```
`juju deploy namecheap-lego-operator --config <yaml config file>`

Relate it to a `tls-certificates-requirer` charm:

`juju relate lego-operator:certificates tls-certificates-requirer`

## Relations

`certificates`: `tls-certificates-interface` provider

## OCI Images

`goacme/lego`

## Contributing

Please see the [Juju SDK docs](https://juju.is/docs/sdk) for guidelines on enhancements to this
charm following best practice guidelines, and
[CONTRIBUTING.md](https://github.com/canonical/namecheap-lego-operator/blob/main/CONTRIBUTING.md) for developer
guidance.
