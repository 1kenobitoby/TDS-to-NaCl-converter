import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Total dissolved solids (TDS) to equivalent NaCl salinity converter",
    page_icon="media/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    #menu_items={
        #'Get Help': '<<URL>>',
        #'Report a bug': "<<URL>>",
        #'About': "Made with Streamlit v1.27.0"
    #}
)

# html strings used to render donate button and link and text
donate_text = '<h6> Useful? Buy us a coffee. </h6>'

html_donate_button = '''
<form action="https://www.paypal.com/donate" method="post" target="_blank">
<input type="hidden" name="hosted_button_id" value="6X8E9CL75SRC2" />
<input type="image" src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button"/>
<img alt="" border="0" src="https://www.paypal.com/en_GB/i/scr/pixel.gif" width="1" height="1" />
</form>
'''   

def redirect_button(url: str):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div>
        <img src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" alt="Donate with PayPal button">
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )


pandas_dataframe = pd.read_csv('k_values.csv')

# convert pandas dataframe to numpy array to use numpy syntax
data = pandas_dataframe.to_numpy()

st.image('media/logo.png', width=100)
st.title('Total dissolved solids (TDS) to equivalent NaCl salinity converter')

st.write('This app converts water sample total dissolved solids multi-ion analyses into equivalent sodium chloride (NaCl) salinities which can then be used to [calculate formation water resistivity (Rw)](https://water-salinity-and-rw-converter.streamlit.app/). Enter your measured ion values in the boxes below. Your ion analyses and TDS should be expressed in either ppm or mg/kg (which are numerically equivalent). If your measured value is expressed in mg/l you\'ll need to convert it using the sample density. Enter as many ions as you have measurements for, leaving the other ones blank. You can safely ignore any ions that you have concentrations measured for which don\'t have an entry box here: these other ions are rarely if ever present in sufficient concentrations in formation waters to have a significant effect on the overall salinity and are usually only measured to help determine how badly contaminated the sample is by mud filtrate. If you need any further explanation, expand the Notes section below')

st.header('Major ions')

l_column, r_column = st.columns([0.5, 0.5])
with l_column:
    ca_ppm = st.number_input(label='Ca\u00B2\u207A concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    mg_ppm = st.number_input(label='Mg\u00B2\u207A concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    k_ppm = st.number_input(label='K\u207A concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    na_ppm = st.number_input(label='Na\u207A concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

with r_column:
    co3_ppm = st.number_input(label='CO\u2083\u00B2\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    so4_ppm = st.number_input(label='SO\u2084\u00B2\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    hco3_ppm = st.number_input(label='HCO\u2083\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    cl_ppm = st.number_input(label='Cl\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

# Same thing as st.divider() which was introduced in recent versions
st.write("---")
st.header('Minor ions')
lm_column, rm_column = st.columns([0.5, 0.5])
with lm_column:
    li_ppm = st.number_input(label='Li\u207A concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    nh4_ppm = st.number_input(label='NH4\u207A concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

with rm_column:
    no3_ppm = st.number_input(label='NO\u2083\u00B2\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    oh_ppm = st.number_input(label='OH\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    br_ppm = st.number_input(label='Br\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

    i_ppm = st.number_input(label='I\u207B concentration in ppm or mg/kg', min_value = 0, max_value=260000, step=1)

if li_ppm >10000 or nh4_ppm >10000 or no3_ppm >10000 or oh_ppm >10000 or br_ppm >10000 or i_ppm >10000:
    st.write('**:red[\*Warning]** This method works for minor ion concentrations <10,000ppm but one or more of your entries is greater than this. We have calculated an equivalent salinity below but it may not be reliable. It is rare to get a minor ion concentration as high as this so you may need to check your water analysis or entries')    

st.write("---")

st.header('Total dissolved solids')
tds_entry = st.number_input(label='**:red[\*Optional]** If your water analysis has a TDS (total dissolved solids) value in either ppm of mg/kg enter it here. The value should be similar to the sum of your ion entries. If you don\'t enter anything, a value will be calculated', min_value = 0, max_value=300000, step=1)

#Put them into a python list
ions = [ca_ppm, mg_ppm, k_ppm, co3_ppm, so4_ppm, hco3_ppm]
nacl_ions = [na_ppm, cl_ppm]
minor_ions = [li_ppm, nh4_ppm, no3_ppm, oh_ppm, br_ppm, i_ppm]
#initialise TDS
tds = 0
tds_sum = 0
  
if tds_entry != 0:
    tds = tds_entry

for i in range(len(ions)):
    tds_sum += ions[i]
for k in range(len(minor_ions)):
    tds_sum += minor_ions[k]    
tds_sum += na_ppm+cl_ppm

if tds_entry != 0 and tds_entry > 1.1*tds_sum or tds_entry != 0 and tds_entry <0.9*tds_sum:
    st.write('**:red[\*Warning]** The TDS value entered in the \'Total Dissolved Solids\' box should be similar to the sum of all your individual ion measurements but yours is significantly different. We\'ve calculated a salinity below based on the values you\'ve entered but you may want to check your water analysis or typing because something looks wrong.')

if tds_entry == 0:
    tds = tds_sum

#Convert to numpy array
ions = np.array(ions)

# Empty list to loop k values into
k_list = []

#Loop through ions, calculating appropriate k values and append to k_list
for j in range(len(ions)):  
    # check whether tds <100 or >200000 and if so, use that kj for this value. Otherwise calculate by interpolation
    if tds<100:
        ki = data[0, j+1]
    elif tds>200000:
        ki=data[40, j+1]
    else:         
# Find the differences between chosen value and every row in ppm column (0)
        difference_array = np.absolute(data[:,0]-tds)

# Find the indices for the 2 lowest values in the difference array (the 2 values either side of the chosen value)
        result = np.argpartition(difference_array, 2)

#make new subset array
        interp_table = data[result[:2]]
        ki = abs(np.min(difference_array)/(interp_table[0,0]-interp_table[1,0]))*(interp_table[1,j+1]-interp_table[0,j+1]) +interp_table[0,j+1]
    k_list.append(ki)

#Calculate equivalent NaCl salinity by multiplying k[i] value * ppm[i] and summing
eq_salinity = 0
for i in range(len(ions)):
    part = ions[i]*k_list[i]
    eq_salinity = eq_salinity + part

#Add Na and Cl ppm values. Calculate & add minor ion contributions
eq_salinity += na_ppm + cl_ppm
eq_salinity += 2.5*li_ppm + 5.5*oh_ppm + 1.9*nh4_ppm + 0.55*no3_ppm + 0.44*br_ppm + 0.28*i_ppm

st.divider()
output_string = '<h3>Your calculated salinity in NaCl equivalent is <span style="color:#F63366;"> ' + "%.0f" % eq_salinity  + 'ppm</span></h3>'
st.markdown(output_string, unsafe_allow_html=True) 

st.write('\n')
st.write('\n')
donate_left, donate_right = st.columns([1, 3])
with donate_left:
    st.write('\n')
    st.markdown(donate_text, unsafe_allow_html=True)

with donate_right:
    st.write('\n')
    redirect_button("https://www.paypal.com/donate/?hosted_button_id=6X8E9CL75SRC2")

st.write('\n')
st.write('\n')
notes = st.button('Notes')

notes_container1 = st.empty()
notes_image = st.empty()
notes_container2 = st.empty()
notes_container3 = st.empty()
notes_container4 = st.empty()
if notes:
    notes_container1.write('This app automates the manual calculations of Baker log interpretation chart \'Equivalent NaCl Concentrations from Total Dissolved Solids Concentrations\' which is the same as Schlumberger chart Gen-8 \'Resistivities of Solutions\' (see below).')
    notes_image.image('media/Baker_TDS.jpg', use_column_width = True)
    notes_container2.write('Saline water conducts electricity because the positive cations are able to accept an electron from the cathode and the negative anions are able to release electrons at the anode, completing the circuit. Different ions have different effects on the overall electrical resistivity of the brine because they have different charges (so can accept and donate different numbers of electrons) and because of they way they interact with one another. The chart takes all the different ion values and converts the Total Dissolved Solids value into an equivalent measure of how saline a pure NaCl brine would have to be to have the same electrochemical behaviour. This NaCl equivalent salinity can then be used in e.g. [Rw calculations & conversions](https://water-salinity-and-rw-converter.streamlit.app/) and petrophysical log interpretations. (If you replicate the example on the chart you will get a slightly different salinity value to the example. That\'s because the example on the chart is using rough k values eye-balled off the graph. This app is calculating them precisely.)')
    notes_container3.write('Overall there should be about as many equivalent anions as cations because the formation water has no electrical potential (i.e. you don\'t get a shock when you put your hand in it). If you got a warning about this, it\'s because your entries don\'t make an electrically neutral solution. This might be because your water analysis is in error or it might be your typing. If you are sure you\'ve entered the values correctly, your water analysis has either measured something incorrectly or hasn\'t measured some ions  that are present and that are having a significant effect on the salinity. To get around the latter problem, some people increase either the Na\u207A or Cl\u207B values until the solution is balanced. However, it\'s a cludge: you don\'t know whether you have ions in the solution that weren\'t measured or whether one of your actual measurements is just too high. In the latter case you are just making the problem worse. Better to get your sample reanalysed or try and find another one.')
    notes_container4.markdown('Your entries have to be in either parts per million (ppm) by weight or mg/kg (which are the same thing because there are 1 million milligrams in a kilogram). If your water analysis quotes everthing by volume (mg/l) then you should convert the values to by weight. At low salinities it doesn\'t matter much: the density of 1 litre of the brine is still very close to 1 million mg/kg. However for a highly saline solution it matters: a salt-saturated brine has about 260,000mg/kg NaCl and a litre of it has a mass of about 1.2kg at room temperature. This is about 260,000 * 1.26 = 310,000mg/l by volume. If you need to convert your inputs from mg/l to mg/kg, just divide them by the specific gravity quoted in your water analysis. Finally while we are confident that this app is correctly implementing the above computations correctly we have no control over the ability of the end user to operate it or correctly interpret and apply the results. In other words, don\'t try and blame us because the prospect you gave a 100% COS to just came in dry.<br><small>*Comments, queries or suggestions? [Contact us](https://www.elephant-stone.com/contact.html)*.</small>', unsafe_allow_html=True)
    hide =st.button('Hide notes')
    if hide:
        notes = not notes
        notes_container1 = st.empty()
        notes_image = st.empty()
        notes_container2 = st.empty()
        notes_container3 = st.empty()
        notes_container4 = st.empty()        
