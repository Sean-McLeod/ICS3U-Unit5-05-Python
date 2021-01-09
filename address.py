#!/usr/bin/env python3

# Created by Sean McLeod
# Created on January 2021
# This program formats an address


def canada_post(addressee, street_number, street_name, city, province,
                postal_code, apt_number=None):
    # this function returns the full Canadian address

    full_address = addressee
    if apt_number != None:
        full_address = (full_address + "\n" + "Apt." + apt_number + " "
                        + street_number + " " + street_name + "\n" + city + " "
                        + province + "  " + ('%.3s' % postal_code) + " "
                        + postal_code[3] + postal_code[4]
                        + postal_code[5] + " ")
    else:
        full_address = (full_address + "\n" + street_number + " " + street_name
                        + "\n" + city + " " + province + "  "
                        + ('%.3s' % postal_code) + " " + postal_code[3]
                        + postal_code[4] + postal_code[5])

    return full_address


def main():
    # gets the needed information and prints it out
    apt_number = None

    print("This program formats a mailing address")
    print("\n")

    # input
    addressee = input("Enter your name: ")
    question = input("Do you have an apartment number? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city = input("Enter your city: ")
    province = input("Enter your province(Ex.Ontario 🡒 ON): ")
    postal_code = input("Enter your postal code(No spaces): ")
    print("\n")

    try:
        street_number_int = int(street_number)

        # call functions
        if apt_number != None:
            final_canada_post = canada_post(addressee, street_number,
                                            street_name, city, province,
                                            postal_code, apt_number)
        else:
            final_canada_post = canada_post(addressee, street_number,
                                            street_name, city, province,
                                            postal_code)
        # output
        print(final_canada_post)

    except Exception:
        print("The Apt.number or the street number is not a number. "
              "Please try again.", "\n")


if __name__ == "__main__":
    main()
