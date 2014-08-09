#!/bin/env python

import sys

# From: the /r/dailyprogrammer challenge:                                                                            
#         http://www.reddit.com/r/dailyprogrammer/comments/2bxntq/7282014_challenge_173_easy_unit_calculator/        


# Define the valid units for the conversion                                                                          
valid_length = ["miles","attoParsecs","inches","meters"]
valid_weight = ["kilograms","pounds","ounces","hogsheads"]


conv = {'miles2attoParsecs': 52155.287, 'miles2inches':63360, 'miles2meters':1609.34,
               'inches2miles': 0.000015783, 'inches2meters': 0.0254, 'inches2attoParsecs': 0.82315794, 
               'meters2miles': 0.000621371, 'meters2inches': 39.3701, 'meters2attoParsecs': 32.4077929,
               'attoParsecs2miles': 0.0000191735116, 'attoParsecs2inches': 1.21483369,
                                                     'attoParsecs2meters': 0.00308567758,
               'kilograms2pounds': 2.20462, 'kilograms2ounces': 35.274, 'kilograms2hogsheads': 0.00226911731337,
               'pounds2kilograms': 0.453592, 'pounds2ounces': 16.0, 'pounds2hogsheads': 0.00102923013586,
               'ounces2kilograms': 0.0283495, 'ounces2pounds': 0.0625, 'ounces2hogsheads': 0.00006432688349,
               'hogsheads2kilograms': 440.7, 'hogsheads2pounds': 971.6, 'hogsheads2ounces': 15545.6}



def get_input():
    """ This method displays the units available and gets user input """

    print("Enter the units to convert and the desired new conversion unit.")
    print("Example: '3 meters to inches'")
    print("Valid length units are inches, attoParsecs, miles, meters.")
    print("Valid weight/mass units are kilograms, pounds, ounces, and hogsheads.")

    listinput = []

    userinput = raw_input('--> ')
    listinput = userinput.split()

    return listinput


def validate_units(userinfo):
    """ validates that the units match, ie don't have one length and one weight unit """

    fromunit = userinfo[1]
    tounit = userinfo[3]

    if fromunit in valid_weight and tounit in valid_weight:
        #print("Both units are valid weight units")
        return True

    if fromunit in valid_length and tounit in valid_length:
        #print("Both units are valid length units")
        return True
    return False           

def validate_input(userinfo):
    """ Validates the input to make sure the syntax was followed """

    try:
        num = int(userinfo[0])
    except ValueError:
        print("Must use whole number units for conversion")
        sys.exit(0)

    if validate_units(userinfo):
        pass
        # print("Units validated")
    else:
        print("%s %s can't be converted to %s" % (userinfo[0], userinfo[1], userinfo[3]))
        sys.exit(0)

    if userinfo[2] != "to":
        print("The syntax is:  N units to units")
        sys.exit(0)

def conversion(userinput):
    """ Converts units as requested """

    numunits = userinput[0]
    fromunit = userinput[1]
    tounit = userinput[3]

    key=fromunit+"2"+tounit

    ans = float(numunits) * conv[key]

    print("%s %s is %f %s" % (numunits, fromunit, ans, tounit))


if __name__ == "__main__":
    userinput = get_input()
    validate_input(userinput)
    conversion(userinput)
