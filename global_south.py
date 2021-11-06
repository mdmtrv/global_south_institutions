import requests
import pandas as pd

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
df = pd.DataFrame(columns=['identifiers', 'instCode', 'instName', 'country'])
for country in global_south:
    url = 'https://api.gbif.org/v1/grscicoll/collection?country='+country
    req = requests.get(url)
    if req.status_code == 200:
        res = req.json()['results']
        for r in res:
            identifiers = []
            identifiers_json = r.get('identifiers')
            for i in identifiers_json:
                identifier = i['identifier']
                identifiers.append(identifier)
            identifiers = ';'.join(identifiers)
            instCode = r.get('institutionCode')
            instName = r.get('institutionName')
            line = {'identifiers': identifiers, 'instCode': instCode, 'instName': instName, 'country': country}
            df = df.append(line, ignore_index=True)
df.to_csv('global_south_collections_institutions.csv', index=False)
