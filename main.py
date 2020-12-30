from flask import Flask, render_template,request
import random
app=Flask(__name__)
@app.route('/random/float/')
def randomfloat():
    return render_template("rfloat.html")
@app.route('/random/float/<low>/<high>/')
def randomfloat_param(low,high):
    return render_template("rfloat.html",low=low,high=high,rand=random.uniform(int(low), int(high)))
@app.route('/random/letter/')
def randomletter():
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return render_template("rletter.html",rand=random.choice(letters))
@app.route('/')
def randompage():
    return render_template("index.html")
@app.route('/random/int/<low>/<high>/')
def randint_param(low,high):
    return render_template("randint.html",low=low,high=high,rand=random.randint(int(low), int(high)))
@app.route('/random/int/')
def randint_no_param():
    return render_template("randint.html")
@app.route('/random/letter/greek/')
def randomgreek():
    letters=["α (alpha)","β (beta)","γ (gamma)","δ (delta)","ε (epsilon)","ζ (zeta)","η (eta)","θ (theta)","ι (iota)","κ (kappa)","λ (lambda)","μ (mu)","ν (nu)","ξ (xi)","ο (omicron)","π (pi)","ρ (rho)","σ (sigma)","τ (tau)","υ (upsilon)","φ (phi)","χ (chi)","ψ (psi)","ω (omega)"]
    return render_template("rgreek.html",rand=random.choice(letters))
@app.route('/random/letter/upper/')
def eng_upper():
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","X"]
    return render_template("rletterupper.html",rand=random.choice(letters))
@app.route('/random/letter/russian/')
def randomrussian():
    letters=["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ","а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я",'й']
    return render_template("rrussian.html",rand=random.choice(letters))
@app.route('/random/dice/')
def dicepage():
    dice=['⚀',  
    '⚁',
    '⚂',
    '⚃',
    '⚄',
    '⚅']
    rand=random.choice(dice)
    rolled=''
    if rand=='⚀':
      rolled='one'
    elif rand=='⚁':
      rolled='two'
    elif rand=='⚂':
      rolled='three'
    elif rand=='⚃':
      rolled='four'
    elif rand=='⚄':
      rolled='five'
    else:
      rolled='six'
    return render_template("dice.html",rand=rand,rolled=rolled)
@app.route('/random/usa/state/')
def randomstate():
    states=['Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming',]
    return render_template("usa_states.html",rand=random.choice(states))
@app.route('/random/canada/')
def random_canada_province_territory():
    states=['Alberta','British Columbia','Ontario','New Brunswick','Prince Edward Island','Newfoundland and Labrador','Saskatchewan','Nova Scotia','Manitoba','Yukon','Northwest Territories','Nunavut']
    return render_template("canada_sub.html",rand=random.choice(states))
@app.route('/random/color/')
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return render_template("color.html",r=r,g=g,b=b)
@app.route('/random/date/')
def random_date():
    months=["January",'February','March','April','June','July','August','September','October','November','December']
    month=random.choice(months)
    day=0
    if month=='January' or month=='March' or month=='May' or month=='July' or month=='August' or month=='October' or month=='December':
      day=random.randint(1,31)
    elif month=='February':
      day=random.randint(1,29)
    else:
      day=random.randint(1,30)
    return render_template("date.html",month=month,day=day)
@app.route('/random/element/')
def random_element():
    elements=((1,	'H',	'Hydrogen'),
    (2,	'He',	'Helium'),
    (3,	'Li',	'Lithium'),
    (4,	'Be',	'Beryllium'),
    (5,	'B',	'Boron'),
    (6,	'C',	'Carbon'),
    (7,	'N',	'Nitrogen'),
    (8,	'O',	'k'),
    (9,	'F',	'Fluorine'),
    (10,	'Ne',	'Neon'),
    (11,	'Na',	'Sodium'),
    (12,	'Mg',	'Magnesium'),
    (13,	'Al',	'Aluminum'),
    (14,	'Si',	'Silicon'),
    (15,	'P',	'Phosphorus'),
    (16,	'S',	'Sulfur'),
    (17,	'Cl',	'Chlorine'),
    (18,	'Ar',	'Argon'),
    (19,	'K',	'Potassium'),
    (20,	'Ca',	'Calcium'),
    (21,	'Sc',	'Scandium'),
    (22,	'Ti',	'Titanium'),
    (23,	'V',	'Vanadium'),
    (24,	'Cr',	'Chromium'),
    (25,	'Mn',	'Manganese'),
    (26,	'Fe',	'Iron'),
    (27,	'Co',	'Cobalt'),
    (28,	'Ni',	'Nickel'),
    (29,	'Cu',	'Copper'),
    (30,	'Zn',	'Zinc'),
    (31,	'Ga',	'Gallium'),
    (32,	'Ge',	'Germanium'),
    (33,	'As',	'Arsenic'),
    (34,	'Se',	'Selenium'),
    (35,	'Br',	'Bromine'),
    (36,	'Kr',	'Krypton'),
    (37,	'Rb',	'Rubidium'),
    (38,	'Sr',	'Strontium'),
    (39,	'Y',	'Yttrium'),
    (40,	'Zr',	'Zirconium'),
    (41,	'Nb',	'Niobium'),
    (42,	'Mo',	'Molybdenum'),
    (43,	'Tc',	'Technetium'),
    (44,	'Ru',	'Ruthenium'),
    (45,	'Rh',	'Rhodium'),
    (46,	'Pd',	'Palladium'),
    (47,	'Ag',	'Silver'),
    (48,	'Cd',	'Cadmium'),
    (49,	'In',	'Indium'),
    (50,	'Sn',	'Tin'),
    (51,	'Sb',	'Antimony'),
    (52,	'Te',	'Tellurium'),
    (53,	'I'	,'Iodine'),
    (54,	'Xe',	'Xenon'),
    (55,	'Cs',	'Cesium'),
    (56,	'Ba',	'Barium'),
    (57,	'La',	'Lanthanum'),
    (58,	'Ce',	'Cerium'),
    (59,	'Pr',	'Praseodymium'),
    (60,	'Nd',	'Neodymium'),
    (61,	'Pm',	'Promethium'),
    (62,	'Sm',	'Samarium'),
    (63,	'Eu',	'Europium'),
    (64,	'Gd',	'Gadolinium'),
    (65,	'Tb',	'Terbium'),
    (66,	'Dy',	'Dysprosium'),
    (67,	'Ho',	'Holmium'),
    (68,	'Er',	'Erbium'),
    (69,	'Tm',	'Thulium'),
    (70,	'Yb',	'Ytterbium'),
    (71,	'Lu',	'Lutetium'),
    (72,	'Hf',	'Hafnium'),
    (73,	'Ta',	'Tantalum'),
    (74,	'W'	,'Tungsten'),
    (75,	'Re',	'Rhenium'),
    (76,	'Os',	'Osmium'),
    (77,	'Ir',	'Iridium'),
    (78,	'Pt',	'Platinum'),
    (79,	'Au',	'Gold'),
    (80,	'Hg',	'Mercury'),
    (81,	'Tl',	'Thallium'),
    (82,	'Pb',	'Lead'),
    (83,	'Bi',	'Bismuth'),
    (84,	'Po',	'Polonium'),
    (85,	'At',	'Astatine'),
    (86,	'Rn',	'Radon'),
    (87,	'Fr',	'Francium'),
    (88,	'Ra',	'Radium'),
    (89,	'Ac',	'Actinium'),
    (90,	'Th',	'Thorium'),
    (91,	'Pa',	'Protactinium'),
    (92,	'U'	,'Uranium'),
    (93,	'Np',	'Neptunium'),
    (94,	'Pu',	'Plutonium'),
    (95,	'Am',	'Americium'),
    (96,	'Cm',	'Curium'),
    (97,	'Bk',	'Berkelium'),
    (98,	'Cf',	'Californium'),
    (99,	'Es',	'Einsteinium'),
    (100,	'Fm',	'Fermium'),
    (101,	'Md',	'Mendelevium'),
    (102,	'No',	'Nobelium'),
    (103,	'Lr',	'Lawrencium'),
    (104,	'Rf',	'Rutherfordium'),
    (105,	'Db',	'Dubnium'),
    (106,	'Sg',	'Seaborgium'),
    (107,	'Bh',	'Bohrium'),
    (108,	'Hs',	'Hassium'),
    (109,	'Mt',	'Meitnerium'),
    (110,	'Ds',	'Darmstadtium'),
    (111,	'Rg',	'Roentgenium'),
    (112,	'Cn',	'Copernicium'),
    (113,	'Nh',	'Nihonium'),
    (114,	'Fl',	'Flerovium'),
    (115,	'Mc',	'Moscovium'),
    (116,	'Lv',	'Livermorium'),
    (117,	'Ts',	'Tennessine'),
    (118,	'Og',	'Oganesson'))
    element=random.choice(elements)[2]
    atomicnum=random.choice(elements)[0]
    symbol=random.choice(elements)[1]
    return render_template("element.html",element=element,atomicnum=atomicnum,symbol=symbol)
@app.route('/random/nba/')
def random_nba():
    teams=['Atlanta Hawks',
    'Boston Celtics',
    'Brooklyn Nets',
    'Charlotte Hornets',
    'Chicago Bulls',
    'Cleveland Cavaliers',
    'Dallas Mavericks',
    'Denver Nuggets',
    'Detroit Pistons',
    'Golden State Warriors',
    'Houston Rockets',
    'Indiana Pacers',
    'Los Angeles Clippers',
    'Los Angeles Lakers',
    'Memphis Grizzlies',
    'Miami Heat',
    'Milwaukee Bucks',
    'Minnesota Timberwolves',
    'New Orleans Pelicans',
    'New York Knicks',
    'Oklahoma City Thunder',
    'Orlando Magic',
    'Philadelphia 76ers',
    'Phoenix Suns',
    'Portland Trail Blazers',
    'Sacramento Kings',
    'San Antonio Spurs',
    'Toronto Raptors',
    'Utah Jazz',
    'Washington Wizards',
    ]
    team=random.choice(teams)
    return render_template("nba.html",team=team)
@app.route('/random/nhl/')
def random_nhl():
    teams=['Anaheim Ducks',
    'Arizona Coyotes',
    'Boston Bruins',
    'Buffalo Sabres',
    'Calgary Flames',
    'Carolina Hurricanes',
    'Chicago Blackhawks',
    'Colorado Avalanche',
    'Columbus Blue Jackets',
    'Dallas Stars',
    'Detroit Red Wings',
    'Edmonton Oilers',
    'Florida Panthers',
    'Los Angeles Kings',
    'Minnesota Wild',
    'Montreal Canadiens',
    'Nashville Predators',
    'New Jersey Devils',
    'New York Islanders',
    'New York Rangers',
    'Ottawa Senators',
    'Philadelphia Flyers',
    'Pittsburgh Penguins',
    'San Jose Sharks',
    'St. Louis Blues',
    'Tampa Bay Lightning',
    'Toronto Maple Leafs',
    'Vancouver Canucks',
    'Vegas Golden Knights',
    'Washington Capitals',
    'Winnipeg Jets',
    ]
    team=random.choice(teams)
    return render_template("nhl.html",team=team)
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)