import xml.etree.cElementTree as ET 
import csv

All_Dict = [] #Declare a list to store all the dictionaries
Store_Xml_Data = {} #Declare a dictionary to store all the values

#push the data to Dictionary
def Push_to_Dictionary(dict_key,dict_value,values_list):
   values_list[len(values_list)]=dict_value
   global Store_Xml_Data
   if dict_key in Store_Xml_Data:
      temp_list=Store_Xml_Data[dict_key]
      temp_list[len(temp_list)]=dict_value
      Store_Xml_Data[dict_key] = temp_list
   else:
      Store_Xml_Data[dict_key] = values_list

#pusing XML tag's attributes to dictionary
def Read_Tags_Attributes(xml_tag,child_attri):
   attr_list={}
   for attr_ke, attr_value in child_attri.items(): 
      attr_key=xml_tag + ':' + attr_ke
      Push_to_Dictionary(attr_key,attr_value,attr_list) 
      attr_list={}

#print recursive function to loop through all the child items
def print_residents(mem):
   values_list={}
   Read_Tags_Attributes(mem.tag,mem.attrib)
   for child in mem:
      #pusing XML tag's attributes to dictionary
      Read_Tags_Attributes(child.tag,child.attrib)
      #pushing XML child tags data to dictionary
      child_count=len(child.getchildren())
      if child_count > 0:
         print_residents(child)
      else:
         if child.text!=None:
            Push_to_Dictionary(child.tag,child.text,values_list)
         values_list={}

#loop through all the top level items
#provide proper tag which you want to read
def process_xmltag(xml_tag_name,root):
   global All_Dict,Store_Xml_Data
   for member in root.findall(xml_tag_name):#'./Stablings_Location/Stabling_Location'): 
      print_residents(member)
      All_Dict.append(Store_Xml_Data)
      Store_Xml_Data={}

#Once you are done collecting data push it into CSV file
def write_to_csv(csv_name):
   with open(csv_name, 'w', newline='') as f:
      # Assuming that all dictionaries in the list have the same keys.
      global All_Dict
      for cnt in range(0,len(All_Dict)):
         headers = [k for k, v in All_Dict[cnt].items()]
      headers = set(headers)
      csv_data = [headers]

      for d in All_Dict:
         csv_data.append([d.get(h,"") for h in headers])

      writer = csv.writer(f)
      writer.writerows(csv_data)
   f.close()

#Assign the XML file to convert to CSV
def convert(xml_file_name,xml_tag_name,csv_name):
   tree = ET.parse(xml_file_name)
   root = tree.getroot() #Get the root of xml file
   process_xmltag(xml_tag_name,root)
   write_to_csv(csv_name)