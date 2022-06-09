# HTMail
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Matteo Golin
A simple mailing program that allows users to send HTML styled emails to a list of addresses.

## Usage
HTML and CSS files that go together must share the same name and be placed in the `/resources` directory.

The HTMLObject just requires the shared name of the HTML and CSS files.

The Email object takes a subject line, plain text to be included in the email, and an HTMLObject instance with the HTML
template to be sent.

The Dispatcher object will take the credentials to the sender email address to provide a secure SSL connection. The 
`.send()` method will take an instance of the Email object and a list of recipient addresses, and then dispatch the
email to all of them.

## Install
- Python 3.10.0 or later

