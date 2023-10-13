# Total dissolved solids (TDS) to equivalent NaCl salinity converter
A web app that allows the user to convert total dissolved solids (TDS) formation water analyses into equivalent NaCl salinities that can then be used for petrophysical interpretations.

# Project description
This is a Streamlit web app written in Python 3.8.10. It implements the equations which govern a graphical method of converting total dissolved solids (TDS) water analyses in equivalent NaCl salinities. This is mainly used in the oil industry for petrophysical interpretation of wireline logs but is also common in hydrogeology.<br>
The app allows the user to enter major and minor ion concentrations and converts the inputs into an equivalent NaCl salinity in parts per million (ppm). It includes a few checks and balances to ensure that the user\'s data looks reliable and warns the user if their sample analysis or typing looks like pish.<br> The calculations done by this app are traditionally done rather laboriously by graphical methods or are sometimes implemented in large integrated petrophysical software packages. The disadvantage of using the latter method is that the packages are expensive so commonly in large companies few licences are available and outside large companies, almost certainly none. Hogging a licence just to perform occasional routine calculations is wasteful and opening and closing the packages constantly is time consuming. This app strips these functions out as a standalone freeby. You\'re welcome. Don\'t forget to say thank you with a donation.<br>
The project has been built in Streamlit V1.27.0 and distributed as a public app on the Streamlit Community Cloud.<br>
There are no plans to develop or update the app (except for bug fixes). Users have the option to contact the authors to suggest changes or improvements which we might implement if we think they are a good idea and it\'s worth our while. But probably not unless they also get their cheque books out.<br>

# How to run the project
Open the URL [https://tds-to-nacl-converter.streamlit.app](https://tds-to-nacl-converter.streamlit.app)

# Dependencies
streamlit (built using V1.26.0)<br>
pandas<br>
numpy<br>


# Licence
The code is copyrighted and no specific licence for its use or distribution is granted. That said, users are welcome to inspect the code, clone the repository and copy code snippets if doing so would help them solve problems with their own projects. But don\'t rip it off wholesale.

