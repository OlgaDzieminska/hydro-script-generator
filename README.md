HYDRO-SCRIPT-GENERATOR

Project is divided into modules:  
1. Dataset repository:  function retrieves all the data from the website based on
 parameters such as the url and path to save.       
2. Dataset provider: prepares all required data to create charts and tables.
   Contists of functions to:
    - find min and max value of water heights and flows in years range
   or for each year in range,
    - provides data for daily flows and states in years,
    - create water height and flow states.
3. Chart generator: pulls required data for generating chart and creates charts
   as images ready to use in output file.
4. Document elements assembler: contains a set of functions for assembling
   hydrological report. These functions adds title page with information
    about the city and river, charts, and headings for document elements.
5. Table generator: creates tables in docx file.

Example of generated table and chart:
![image](https://github.com/OlgaDzieminska/hydro-script-generator/assets/93330676/a5764d14-89b5-48c9-846e-d1381b99e198)



![image](https://github.com/OlgaDzieminska/hydro-script-generator/assets/93330676/ccd82f02-bf1b-4a2f-ad25-b8e144730adc)
