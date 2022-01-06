from numpy.core.numeric import NaN
import requests
import pandas as pd
import pycountry
df = pd.read_csv('institutional_use_counts_global_countries.csv')
global_south_africa = [
'Angola',
'Benin',
'Botswana',
'Burkina Faso', 'Burundi',
'Cameroon',
'Cape Verde',
'Central African Republic',
'Chad',
'Congo',
'The Democratic Republic of Congo',
'Côte D’Ivoire',
'Equatorial Guinea',
'Eritrea',
'Ethiopia',
'Gabon',
'Gambia',
'Ghana',
'Guinea',
'Guinea-Bissau',
'Kenya',
'Lesotho',
'Liberia' 'Madagascar',
'Malawi',
'Mali',
'Mauritius',
'Mayotte',
'Mozambique',
'Namibia',
'Niger',
'Nigeria',
'Rwanda',
'Saint Helena',
'Sao Tome and Principe',
'Senegal',
'Seychelles',
'Sierra Leone',
'South Africa',
'South Sudan',
'Swaziland',
'Tanzania',
'Togo',
'Uganda',
'Western Sahara',
'Zambia',
'Zimbabwe'
]

global_south_arab = [
'Algeria',
'Bahrain',
'Comoros',
'Djibouti',
'Egypt',
'Iraq',
'Jordan',
'Kuwait',
'Lebanon',
'Libya',
'Mauritania',
'Morocco',
'Oman',
'Palestinian Territory',
'Qatar',
'Saudi Arabia',
'Somalia',
'Sudan',
'Tunisia',
'United Arab Emirates',
'Yemen'
]

global_south_asia = [
'Afghanistan',
'American Somoa',
'Antarctica',
'Azerbaijan',
'Bangladesh',
'Bhutan',
'British Indian Ocean Territory',
'Brunei Darussalam',
'Cambodia',
'China',
'Christmas Island',
'Cocos (Keeling) Islands',
'Cook Islands',
'Fiji',
'French Polynesia',
'French Southern Territories',
'Guam',
'Heard Island and McDonald Islands',
'India',
'Indonesia',
'Iran',
'Kazakhstan',
'Kiribati',
'(Democratic People’s Republic of North) Korea',
'Kyrgyzstan',
'Lao',
'Macau',
'Malaysia',
'Maldives',
'Marshall Islands',
'Micronesia',
'Mongolia',
'Nauru',
'Nepal',
'New Caledonia',
'Niue',
'Norfolk Island',
'Northern Mariana Islands',
'Pakistan',
'Palau',
'Papua New Guinea',
'Philippines',
'Pitcairn Islands',
'Reunion',
'Samoa',
'Solomon Islands',
'Sri Lanka',
'Syrian Arab Emirates',
'Tajikistan',
'Thailand',
'Timor-Leste',
'Tokelau',
'Tonga',
'Turkmenistan',
'Tuvalu',
'United States Minor Outlying Islands',
'Uzbekistan',
'Vanuatu',
'Vietnam',
'Wallis and Futuna'
]

global_south_europe = [
'Armenia',
'Belarus',
'Georgia',
'Ukraine'
]

global_south_samerica = [
'Anguilla',
'Antigua and Barbuda',
'Argentina',
'Aruba',
'Bahamas',
'Barbados',
'Belize',
'Bolivia',
'Bouvet Island',
'Brazil',
'Cayman Islands',
'Chile',
'Colombia',
'Costa Rica',
'Cuba',
'Dominica',
'Dominican Republic',
'Ecuador',
'El Salvador',
'Falkland Islands',
'French Guiana',
'Granada',
'Guadeloupe',
'Guatemala',
'Guyana',
'Haiti',
'Honduras',
'Jamaica',
'Martinique',
'Mexico',
'Montserrat',
'Netherlands Antilles',
'Nicaragua',
'Panama',
'Paraguay',
'Peru',
'Puerto Rico',
'Saint Barthelemy',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Martin',
'Saint Vincent and Grenadines',
'South Georgia and the South Sandwich Islands',
'Suriname'
'Trinidad and Tobago',
'Turks and Caicos Islands',
'Uruguay',
'Venezuela',
'Virgin Island (British)',
'Virgin Islands (US)'
]

global_south = global_south_africa+global_south_arab+global_south_asia+global_south_europe+global_south_samerica


for index, row in df.iterrows():
    country = row['country']
    if country is not NaN:
        if len(country) == 3:
            country_name = pycountry.countries.get(alpha_3=country).name
        elif len(country) == 2:
            country_name = pycountry.countries.get(alpha_2=country).name
        else:
            country_name = country
        df.loc[index, 'country_name'] = country_name
        if country_name in global_south:
            df.loc[index, 'region'] = "GS"
        else:
            df.loc[index, 'region'] = "GN"
    else:
        df.loc[index, 'region'] = NaN
        df.loc[index, 'country_name'] = NaN

df.to_csv('final_results.csv', index=False)
