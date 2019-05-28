# Python_XML_to_CSV
This python code will convert any type of XML file’s specific tag data to csv file irrespective of tag names. It will generate all the attributes and child tag values and attribute information.
So, for readability I strongly suggest to pass specific tag name, eventually this code will generate individual line in csv file for individual specific tag.
Here is the function Name & Param:
Built In Function name: Convert
Params: xml_file_name – Xml file path
	 xml_tag_name – Tag which we need to convert
               csv_name – csv file complete path with name

XML: https://docs.microsoft.com/en-us/dotnet/visual-basic/programming-guide/concepts/linq/sample-xml-file-multiple-purchase-orders-linq-to-xml
BIF example: convert("C:\\Users\\Python\\sample.xml","./PurchaseOrder", "C:\\Users\\Python\\output.csv")
Output: Output csv file is attached.
