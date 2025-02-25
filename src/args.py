#TASK 3
import argparse
import ipaddress

def check_port(val):
    '''
        Description
        -This function validate the port number, number of siffer and as it in the valid format
        Param
        -Val: port number to validate
        Returns
        -Port number as an integers
        Raises
        -argparse.ArgumentTypeError: If the input is not a valid integer or is out of the allowed range.
    '''
    try:
        value = int(val)
    except ValueError:
        raise argparse.ArgumentTypeError('An integer are required for port number')
    if value not in range(1024, 65535 + 1):
        raise argparse.ArgumentTypeError("Invalid port. It must be within the range [1024,65535]")
    return value

def check_ip(address):
    """
    Description:
    Validates the IP address to ensure it is in the correct format
    Parameters:
    -address: The IP address to validate
    Returns:
    -The validated IP address as a string
    Raises:
    -argparse.ArgumentTypeError: If the input is not a valid IP address
    """
    try:
        val = ipaddress.ip_address(address)
        return val
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid IP.  It must in this format: 10.1.2.3")



parser = argparse.ArgumentParser(description="A tool to run in either server or client mode.")


parser.add_argument("-s", "--server", help="enable the server mode",
                    action="store_true")
parser.add_argument("-c", "--client", help="enable the client mode",
                    action="store_true")
parser.add_argument("-p", "--port", help="allows to select port number on which the server will listen; the port must be an integer and in the range [1024, 65535], default: 8088.",
                    type=check_port, default=8088)
parser.add_argument("-i", "--ip", type=check_ip, default="10.0.0.2",
                    help="allows to select the ip address of the server’s interface where the client should connect. Use a default value if it’s not provided. It must be in the dotted decimal notation format, e.g. 10.0.0.2 and each block should be in the range of [0,255].")

args = parser.parse_args()
#check if both args use it
if args.server and args.client: 
    parser.error("You cannot use both at the same")
#check if non of args use it
elif not args.server and not args.client:
    parser.error("You should run either in server or client mode")
else:
    mode = "server" if args.server else "client"
    print(f"The {mode} is running with IP address = {args.ip} and port address = {args.port}")