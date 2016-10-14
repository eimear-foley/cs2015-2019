"""Lab 3 - Writing of subclass 'Business' of super class 'Property'
	Includes:
		- addition of extra instance variables: companyName, businessType
		- 'Property' class's getAddress should be overridden to include companyName
"""

from property import Property

class Business(object):

    def __init__(self, floorarea, address, companyName, businessType):
        Property.__init__(self, floorarea, address)
        self._companyName = companyName
        self._businessType = businessType

    def getAddress(self):
        return ("%s, %s" %(self._companyName, businessType))

    def setCompanyName(self, companyName):
        self._companyName = companyName

    def getCompanyName(self):
        return self._companyName

    def setBusinessType(self, businessType):
        self._businessType = businessType

    def getBusinessType(self):
        return self._businessType

    def __str__(self):
        return("Business Name: %s, Business Address: %s. Business Type: %s, Floor Area: %i" % (self._companyName, self._address, self._businessType, self._floorarea))

    address = property(getAddress, Property.setAddress)
    company_name = property(getCompanyName, setCompanyName)
    business_type = property(getBusinessType, setBusinessType)

def main():

    business = Business(1200, "Western Rd", "Insight Centre for Data Analytics", "IT")
    print(business)

    business.company_name = "Ignite"
    business.address = "Western Road, Cork"
    business.business_type = "Inovation"
    print(business)


if __name__ == "__main__":
    main()
