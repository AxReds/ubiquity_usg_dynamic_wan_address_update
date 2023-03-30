# Ubiquiti USG WAN IP Updater

This is a script that automatically updates the WAN IP address of a Ubiquiti USG router whenever it changes. It can be run on a separate machine and uses either Bash or Python, depending on your preference.

## Bash version

The Bash version of the script uses the `curl` command to get the current WAN IP address and the Ubiquiti EdgeOS CLI to update the router configuration. It can be run on any system that has Bash and the `sshpass` package installed.

## Python version

The Python version of the script uses the `requests` library to get the current WAN IP address and the Paramiko library to SSH into the Ubiquiti router and update the configuration. It can be run on any system that has Python and the `paramiko` and `requests` packages installed.

## Usage

To use the script, you'll need to modify the variables at the top of the file to match your own router configuration. Once you've done that, you can simply run the script and it will automatically update the WAN IP address whenever it changes.

## License

This project is licensed under the GNU v3.0 License.

Feel free to use and modify this script as you see fit. If you find any issues or have any suggestions for improvement, please feel free to open an issue or submit a pull request.
