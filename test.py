from pprint import pprint
import json

major_list = [
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.5, 'Draw': 3.85, 'Away Wins': 1.75,
     'Away Team': 'Cangzhou Mighty Lions SRL', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.3, 'Draw': 3.7, 'Away Wins': 1.67,
     'Away Team': 'Cangzhou Mighty Lions Srl', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.4, 'Draw': 3.8, 'Away Wins': 1.7,
     'Away Team': 'Cangzhou Mighty Lions Srl', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.58, 'Draw': 3.94, 'Away Wins': 1.73,
     'Away Team': 'Cangzhou Mighty Lions Srl', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.85, 'Away Wins': 1.7,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River', 'Commence Time': '14:30:00', 'Home Wins': 4.78, 'Draw': 4.08,
     'Away Wins': 1.685, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9,
     'Away Wins': 1.7, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban', 'Commence Time': '10:30:00', 'Home Wins': 3.0, 'Draw': 3.2,
     'Away Wins': 2.2, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban', 'Commence Time': '10:30:00', 'Home Wins': 3.1, 'Draw': 3.25,
     'Away Wins': 2.25, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban', 'Commence Time': '10:30:00', 'Home Wins': 3.128, 'Draw': 3.132,
     'Away Wins': 2.292, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban F.C', 'Commence Time': '10:30:00', 'Home Wins': 3.0, 'Draw': 3.2,
     'Away Wins': 2.2, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban FC', 'Commence Time': '10:30:00', 'Home Wins': 2.85, 'Draw': 2.95,
     'Away Wins': 2.2, 'Away Team': 'Suzhou Dongwu FC', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shenyang City', 'Commence Time': '10:30:00', 'Home Wins': 3.1, 'Draw': 3.3, 'Away Wins': 2.26,
     'Away Team': 'Jinfu', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Shenyang City FC', 'Commence Time': '10:30:00', 'Home Wins': 3.04, 'Draw': 3.29, 'Away Wins': 2.24,
     'Away Team': 'Suzhou Dongwu FC', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Shenyang Urban FC', 'Commence Time': '10:30:00', 'Home Wins': 2.9, 'Draw': 3.2, 'Away Wins': 2.15,
     'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Hebei KungFu', 'Commence Time': '10:30:00', 'Home Wins': 1.05, 'Draw': 9.5, 'Away Wins': 19.0,
     'Away Team': 'Beijing Tech FC', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Hebei KungFu', 'Commence Time': '10:30:00', 'Home Wins': 1.06, 'Draw': 9.0, 'Away Wins': 19.0,
     'Away Team': 'Beijing Institute of Technology FC', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shijiazhuang Gongfu', 'Commence Time': '10:30:00', 'Home Wins': 1.06, 'Draw': 10.5,
     'Away Wins': 25.0, 'Away Team': 'Beijing Institute of Technology', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shijiazhuang Gongfu FC', 'Commence Time': '10:30:00', 'Home Wins': 1.08, 'Draw': 10.0,
     'Away Wins': 24.0, 'Away Team': 'Beijing Ligong', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Shijiazhuang Gongfu FC', 'Commence Time': '10:30:00', 'Home Wins': 1.07, 'Draw': 9.6,
     'Away Wins': 22.0, 'Away Team': 'Beijing Institute of Technology', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.89, 'Draw': 3.3, 'Away Wins': 3.75,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.95, 'Draw': 3.4, 'Away Wins': 3.85,
     'Away Team': 'Chengdu Rongcheng FC SRL', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.89, 'Draw': 3.3, 'Away Wins': 3.75,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.92, 'Draw': 3.35, 'Away Wins': 3.8,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.96, 'Draw': 3.48, 'Away Wins': 3.95,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai East Asia', 'Commence Time': '12:30:00', 'Home Wins': 1.8, 'Draw': 3.4, 'Away Wins': 4.6,
     'Away Team': 'Chengdu Better City FC', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai East Asia', 'Commence Time': '12:30:00', 'Home Wins': 1.7, 'Draw': 3.3, 'Away Wins': 4.0,
     'Away Team': 'Chengdu Better City', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port', 'Commence Time': '12:30:00', 'Home Wins': 1.8, 'Draw': 3.6, 'Away Wins': 4.25,
     'Away Team': 'Chengdu Qianbao', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port', 'Commence Time': '12:30:00', 'Home Wins': 1.784, 'Draw': 3.76, 'Away Wins': 4.5,
     'Away Team': 'Chengdu Rongcheng', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port FC', 'Commence Time': '12:30:00', 'Home Wins': 1.8, 'Draw': 3.6, 'Away Wins': 4.3,
     'Away Team': 'Chengdu Better City', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port FC', 'Commence Time': '12:30:00', 'Home Wins': 1.82, 'Draw': 3.7, 'Away Wins': 4.4,
     'Away Team': 'Chengdu Rongcheng', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.85, 'Away Wins': 1.7,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River', 'Commence Time': '14:30:00', 'Home Wins': 4.78, 'Draw': 4.08,
     'Away Wins': 1.685, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9,
     'Away Wins': 1.7, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.7, 'Draw': 3.9, 'Away Wins': 1.69,
     'Away Team': 'Shijiazhuang', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9, 'Away Wins': 1.65,
     'Away Team': 'Shijiazhuang Yongchang FC', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9, 'Away Wins': 1.68,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.5, 'Draw': 3.75, 'Away Wins': 1.61,
     'Away Team': 'Shijiazhuang Yongchang FC', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC', 'Commence Time': '14:30:00', 'Home Wins': 4.7, 'Draw': 3.9, 'Away Wins': 1.69,
     'Away Team': 'Shijiazhuang', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC', 'Commence Time': '14:30:00', 'Home Wins': 4.4, 'Draw': 3.6, 'Away Wins': 1.57,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Akhmat', 'Commence Time': '15:00:00', 'Home Wins': 2.42, 'Draw': 3.52, 'Away Wins': 2.98,
     'Away Team': 'Rostov', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.37, 'Draw': 3.41, 'Away Wins': 2.91,
     'Away Team': 'FC Rostov', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.35, 'Draw': 3.3, 'Away Wins': 2.85,
     'Away Team': 'Rostov', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'RFK Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.3, 'Draw': 3.33, 'Away Wins': 2.85,
     'Away Team': 'FK Rostov', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Republican Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.3, 'Draw': 3.3,
     'Away Wins': 2.8, 'Away Team': 'Rostov', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'CA River Plate (Arg)', 'Commence Time': '16:00:00', 'Home Wins': 2.22, 'Draw': 3.21,
     'Away Wins': 2.92, 'Away Team': 'Argentinos Juniors Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'CA River Plate (Arg)', 'Commence Time': '16:00:00', 'Home Wins': 2.26, 'Draw': 3.25,
     'Away Wins': 2.95, 'Away Team': 'Argentinos Juniors Reserve', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'CA River Plate (Arg)', 'Commence Time': '16:00:00', 'Home Wins': 2.25, 'Draw': 3.2, 'Away Wins': 2.9,
     'Away Team': 'Argentinos Juniors Reserve', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'River Plate', 'Commence Time': '16:00:00', 'Home Wins': 2.24, 'Draw': 3.2, 'Away Wins': 2.9,
     'Away Team': 'Argentinos', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'River Plate II', 'Commence Time': '16:00:00', 'Home Wins': 2.248, 'Draw': 3.24, 'Away Wins': 2.975,
     'Away Team': 'Argentinos Juniors II', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico', 'Commence Time': '17:00:00', 'Home Wins': 1.73, 'Draw': 3.55, 'Away Wins': 4.2,
     'Away Team': 'Patronato Res.', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman (Res)', 'Commence Time': '17:00:00', 'Home Wins': 1.66, 'Draw': 3.5,
     'Away Wins': 4.0, 'Away Team': 'CA Patronato (Res)', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.71, 'Draw': 3.55,
     'Away Wins': 4.22, 'Away Team': 'Patronato Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.75, 'Draw': 3.6,
     'Away Wins': 4.25, 'Away Team': 'CA Patronato Parana Reserve', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.85, 'Draw': 3.6,
     'Away Wins': 3.4, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.74, 'Draw': 3.6,
     'Away Wins': 4.2, 'Away Team': 'CA Patronato Parana', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.74, 'Draw': 3.55,
     'Away Wins': 4.2, 'Away Team': 'CA Patronato Parana', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.73, 'Draw': 3.6,
     'Away Wins': 4.2, 'Away Team': 'CA Patronato Parana', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Aldosivi', 'Commence Time': '17:00:00', 'Home Wins': 2.55, 'Draw': 3.2, 'Away Wins': 2.5,
     'Away Team': 'Tigre', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.57, 'Draw': 3.2, 'Away Wins': 2.53,
     'Away Team': 'Tigre Reserve', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.54, 'Draw': 3.22, 'Away Wins': 2.5,
     'Away Team': 'CA Tigre Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.6, 'Draw': 3.25, 'Away Wins': 2.6,
     'Away Team': 'CA TIGRE', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.6, 'Draw': 3.25, 'Away Wins': 2.55,
     'Away Team': 'CA Tigre Reserve', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.55, 'Draw': 3.2, 'Away Wins': 2.5,
     'Away Team': 'CA Tigre Reserve', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Colon Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.28, 'Draw': 3.1,
     'Away Wins': 2.95, 'Away Team': 'Estudiantes', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe II', 'Commence Time': '17:00:00', 'Home Wins': 2.245, 'Draw': 3.165,
     'Away Wins': 3.045, 'Away Team': 'Estudiantes II', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.26, 'Draw': 3.07,
     'Away Wins': 2.97, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.15,
     'Away Wins': 3.05, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.1,
     'Away Wins': 3.0, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.1,
     'Away Wins': 2.96, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.1,
     'Away Wins': 2.95, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Fakel Voronezh', 'Commence Time': '17:30:00', 'Home Wins': 3.1, 'Draw': 3.4, 'Away Wins': 2.15,
     'Away Team': 'PFK Krylia Sovetov Samara', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel', 'Commence Time': '17:30:00', 'Home Wins': 3.11, 'Draw': 3.51, 'Away Wins': 2.21,
     'Away Team': 'Kryliya Sovetov', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Voronezh', 'Commence Time': '17:30:00', 'Home Wins': 3.0, 'Draw': 3.35, 'Away Wins': 2.14,
     'Away Team': 'Krylia Sovetov Samara', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Voronezh', 'Commence Time': '17:30:00', 'Home Wins': 3.144, 'Draw': 3.64, 'Away Wins': 2.27,
     'Away Team': 'Krylia Sovetov', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Worenesch', 'Commence Time': '17:30:00', 'Home Wins': 3.05, 'Draw': 3.4, 'Away Wins': 2.15,
     'Away Team': 'Kryliya Sovetov', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Worenesch', 'Commence Time': '17:30:00', 'Home Wins': 2.45, 'Draw': 3.25, 'Away Wins': 2.55,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Worenesch', 'Commence Time': '17:30:00', 'Home Wins': 3.05, 'Draw': 3.4, 'Away Wins': 2.2,
     'Away Team': 'Kryliya Sovetov Samara', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'FC Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.8, 'Draw': 3.3, 'Away Wins': 2.7,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.2, 'Away Wins': 2.6,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.62, 'Draw': 3.2, 'Away Wins': 2.5,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.71, 'Draw': 3.2, 'Away Wins': 2.61,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.15, 'Away Wins': 2.6,
     'Away Team': 'HJK', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.15, 'Away Wins': 2.65,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.15, 'Away Wins': 2.67,
     'Away Team': 'HJK', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.55, 'Draw': 2.95, 'Away Wins': 2.45,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.71, 'Draw': 3.28, 'Away Wins': 2.57,
     'Away Team': 'HJK', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab Club', 'Commence Time': '18:00:00', 'Home Wins': 2.3, 'Draw': 3.06, 'Away Wins': 2.92,
     'Away Team': 'Shabab Al Ordun', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab Club', 'Commence Time': '18:00:00', 'Home Wins': 2.26, 'Draw': 3.096, 'Away Wins': 3.12,
     'Away Team': 'Shabab Al Ordon Al Quadisiya', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.34, 'Draw': 3.1, 'Away Wins': 2.95,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.35, 'Draw': 3.05, 'Away Wins': 3.05,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.35, 'Draw': 3.05, 'Away Wins': 2.92,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.35, 'Draw': 3.1, 'Away Wins': 3.0,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.3, 'Draw': 3.0, 'Away Wins': 3.0,
     'Away Team': 'Shabab Al-Ordon', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat', 'Commence Time': '18:30:00', 'Home Wins': 1.47, 'Draw': 4.3, 'Away Wins': 5.4,
     'Away Team': 'Maccabi Girls Emek Hefer', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat (Women)', 'Commence Time': '18:30:00', 'Home Wins': 1.44, 'Draw': 4.4, 'Away Wins': 5.9,
     'Away Team': 'Maccabi Emek Hefer (Women)', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat SC', 'Commence Time': '18:30:00', 'Home Wins': 1.46, 'Draw': 4.2, 'Away Wins': 5.2,
     'Away Team': 'Maccabi Girls Emek Hefer', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat SC', 'Commence Time': '18:30:00', 'Home Wins': 1.44, 'Draw': 4.1, 'Away Wins': 5.1,
     'Away Team': 'Maccabi Girls Emek Hefer', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich', 'Commence Time': '20:00:00', 'Home Wins': 1.17, 'Draw': 6.4, 'Away Wins': 13.0,
     'Away Team': 'Real Sociedad San Sebastian', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich', 'Commence Time': '20:00:00', 'Home Wins': 1.19, 'Draw': 6.3, 'Away Wins': 12.0,
     'Away Team': 'Real Sociedad San Sebastian', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich (W)', 'Commence Time': '20:00:00', 'Home Wins': 1.16, 'Draw': 6.7, 'Away Wins': 13.0,
     'Away Team': 'Real Sociedad (W)', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich W', 'Commence Time': '20:00:00', 'Home Wins': 1.14, 'Draw': 6.68, 'Away Wins': 13.36,
     'Away Team': 'Real Sociedad W', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich W', 'Commence Time': '20:00:00', 'Home Wins': 1.18, 'Draw': 6.5, 'Away Wins': 13.0,
     'Away Team': 'Real Sociedad San Sebastian', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Everton', 'Commence Time': '20:30:00', 'Home Wins': 1.43, 'Draw': 4.4, 'Away Wins': 5.8,
     'Away Team': 'Leicester City WFC', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Everton (W)', 'Commence Time': '20:30:00', 'Home Wins': 1.45, 'Draw': 4.5, 'Away Wins': 6.0,
     'Away Team': 'Leicester (W)', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Everton FC', 'Commence Time': '20:30:00', 'Home Wins': 1.42, 'Draw': 4.3, 'Away Wins': 5.6,
     'Away Team': 'Leicester City Ladies', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Everton FC', 'Commence Time': '20:30:00', 'Home Wins': 1.43, 'Draw': 4.4, 'Away Wins': 5.7,
     'Away Team': 'Leicester City WFC', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.3, 'Draw': 3.11, 'Away Wins': 2.08,
     'Away Team': 'Jazeera Amman', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.35, 'Draw': 3.15, 'Away Wins': 2.12,
     'Away Team': 'Al Jazeera Jordan', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.35, 'Draw': 3.2, 'Away Wins': 2.15,
     'Away Team': 'Al Jazeera Club Jordan', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.4, 'Draw': 3.2, 'Away Wins': 2.15,
     'Away Team': 'AL Jazeera Club Amman', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.3, 'Draw': 3.1, 'Away Wins': 2.1,
     'Away Team': 'AL Jazeera Club Amman', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.24, 'Draw': 3.32, 'Away Wins': 2.098,
     'Away Team': 'Al-Jazeera Amman', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.44, 'Draw': 3.1, 'Away Wins': 2.6,
     'Away Team': 'Montana 1921', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.45, 'Draw': 3.1, 'Away Wins': 2.65,
     'Away Team': 'PFC Montana 1921', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Maritsa', 'Commence Time': '17:00:00', 'Home Wins': 2.47, 'Draw': 3.15, 'Away Wins': 2.65,
     'Away Team': 'Montana', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.55, 'Draw': 3.15, 'Away Wins': 2.7,
     'Away Team': 'PFC Montana 1921', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.496, 'Draw': 3.2, 'Away Wins': 2.582,
     'Away Team': 'Montana', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'}
]

# TODO Sort based on time and home team
# sorted_matches_list = sorted(major_list, key=lambda match_dict: (match_dict['Commence Time'], match_dict['Home Team'],  match_dict['Home Wins']))
# for match in sorted_matches_list:
#     print(match)

sorted_matches_list = [
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.89, 'Draw': 3.3, 'Away Wins': 3.75,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.89, 'Draw': 3.3, 'Away Wins': 3.75,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.92, 'Draw': 3.35, 'Away Wins': 3.8,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.95, 'Draw': 3.4, 'Away Wins': 3.85,
     'Away Team': 'Chengdu Rongcheng FC SRL', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Sipg SRL', 'Commence Time': '08:00:00', 'Home Wins': 1.96, 'Draw': 3.48, 'Away Wins': 3.95,
     'Away Team': 'Chengdu Rongcheng FC Srl', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.3, 'Draw': 3.7, 'Away Wins': 1.67,
     'Away Team': 'Cangzhou Mighty Lions Srl', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.4, 'Draw': 3.8, 'Away Wins': 1.7,
     'Away Team': 'Cangzhou Mighty Lions Srl', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.5, 'Draw': 3.85, 'Away Wins': 1.75,
     'Away Team': 'Cangzhou Mighty Lions SRL', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC SRL', 'Commence Time': '08:00:00', 'Home Wins': 4.58, 'Draw': 3.94, 'Away Wins': 1.73,
     'Away Team': 'Cangzhou Mighty Lions Srl', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Hebei KungFu', 'Commence Time': '10:30:00', 'Home Wins': 1.05, 'Draw': 9.5, 'Away Wins': 19.0,
     'Away Team': 'Beijing Tech FC', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Hebei KungFu', 'Commence Time': '10:30:00', 'Home Wins': 1.06, 'Draw': 9.0, 'Away Wins': 19.0,
     'Away Team': 'Beijing Institute of Technology FC', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban', 'Commence Time': '10:30:00', 'Home Wins': 3.0, 'Draw': 3.2,
     'Away Wins': 2.2, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban', 'Commence Time': '10:30:00', 'Home Wins': 3.1, 'Draw': 3.25,
     'Away Wins': 2.25, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban', 'Commence Time': '10:30:00', 'Home Wins': 3.128, 'Draw': 3.132,
     'Away Wins': 2.292, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban F.C', 'Commence Time': '10:30:00', 'Home Wins': 3.0, 'Draw': 3.2,
     'Away Wins': 2.2, 'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Liaoning Shenyang Urban FC', 'Commence Time': '10:30:00', 'Home Wins': 2.85, 'Draw': 2.95,
     'Away Wins': 2.2, 'Away Team': 'Suzhou Dongwu FC', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shenyang City', 'Commence Time': '10:30:00', 'Home Wins': 3.1, 'Draw': 3.3, 'Away Wins': 2.26,
     'Away Team': 'Jinfu', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Shenyang City FC', 'Commence Time': '10:30:00', 'Home Wins': 3.04, 'Draw': 3.29, 'Away Wins': 2.24,
     'Away Team': 'Suzhou Dongwu FC', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Shenyang Urban FC', 'Commence Time': '10:30:00', 'Home Wins': 2.9, 'Draw': 3.2, 'Away Wins': 2.15,
     'Away Team': 'Suzhou Dongwu', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shijiazhuang Gongfu', 'Commence Time': '10:30:00', 'Home Wins': 1.06, 'Draw': 10.5,
     'Away Wins': 25.0, 'Away Team': 'Beijing Institute of Technology', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shijiazhuang Gongfu FC', 'Commence Time': '10:30:00', 'Home Wins': 1.07, 'Draw': 9.6,
     'Away Wins': 22.0, 'Away Team': 'Beijing Institute of Technology', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Shijiazhuang Gongfu FC', 'Commence Time': '10:30:00', 'Home Wins': 1.08, 'Draw': 10.0,
     'Away Wins': 24.0, 'Away Team': 'Beijing Ligong', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai East Asia', 'Commence Time': '12:30:00', 'Home Wins': 1.7, 'Draw': 3.3, 'Away Wins': 4.0,
     'Away Team': 'Chengdu Better City', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai East Asia', 'Commence Time': '12:30:00', 'Home Wins': 1.8, 'Draw': 3.4, 'Away Wins': 4.6,
     'Away Team': 'Chengdu Better City FC', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port', 'Commence Time': '12:30:00', 'Home Wins': 1.784, 'Draw': 3.76, 'Away Wins': 4.5,
     'Away Team': 'Chengdu Rongcheng', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port', 'Commence Time': '12:30:00', 'Home Wins': 1.8, 'Draw': 3.6, 'Away Wins': 4.25,
     'Away Team': 'Chengdu Qianbao', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port FC', 'Commence Time': '12:30:00', 'Home Wins': 1.8, 'Draw': 3.6, 'Away Wins': 4.3,
     'Away Team': 'Chengdu Better City', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Shanghai Port FC', 'Commence Time': '12:30:00', 'Home Wins': 1.82, 'Draw': 3.7, 'Away Wins': 4.4,
     'Away Team': 'Chengdu Rongcheng', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.85, 'Away Wins': 1.7,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.85, 'Away Wins': 1.7,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River', 'Commence Time': '14:30:00', 'Home Wins': 4.78, 'Draw': 4.08,
     'Away Wins': 1.685, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River', 'Commence Time': '14:30:00', 'Home Wins': 4.78, 'Draw': 4.08,
     'Away Wins': 1.685, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9,
     'Away Wins': 1.7, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Yangtze River FC', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9,
     'Away Wins': 1.7, 'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.5, 'Draw': 3.75, 'Away Wins': 1.61,
     'Away Team': 'Shijiazhuang Yongchang FC', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.7, 'Draw': 3.9, 'Away Wins': 1.69,
     'Away Team': 'Shijiazhuang', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9, 'Away Wins': 1.65,
     'Away Team': 'Shijiazhuang Yongchang FC', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall', 'Commence Time': '14:30:00', 'Home Wins': 4.75, 'Draw': 3.9, 'Away Wins': 1.68,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC', 'Commence Time': '14:30:00', 'Home Wins': 4.4, 'Draw': 3.6, 'Away Wins': 1.57,
     'Away Team': 'Cangzhou Mighty Lions', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Wuhan Zall FC', 'Commence Time': '14:30:00', 'Home Wins': 4.7, 'Draw': 3.9, 'Away Wins': 1.69,
     'Away Team': 'Shijiazhuang', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Akhmat', 'Commence Time': '15:00:00', 'Home Wins': 2.42, 'Draw': 3.52, 'Away Wins': 2.98,
     'Away Team': 'Rostov', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.35, 'Draw': 3.3, 'Away Wins': 2.85,
     'Away Team': 'Rostov', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.37, 'Draw': 3.41, 'Away Wins': 2.91,
     'Away Team': 'FC Rostov', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'RFK Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.3, 'Draw': 3.33, 'Away Wins': 2.85,
     'Away Team': 'FK Rostov', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Republican Akhmat Grozny', 'Commence Time': '15:00:00', 'Home Wins': 2.3, 'Draw': 3.3,
     'Away Wins': 2.8, 'Away Team': 'Rostov', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'CA River Plate (Arg)', 'Commence Time': '16:00:00', 'Home Wins': 2.22, 'Draw': 3.21,
     'Away Wins': 2.92, 'Away Team': 'Argentinos Juniors Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'CA River Plate (Arg)', 'Commence Time': '16:00:00', 'Home Wins': 2.25, 'Draw': 3.2, 'Away Wins': 2.9,
     'Away Team': 'Argentinos Juniors Reserve', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'CA River Plate (Arg)', 'Commence Time': '16:00:00', 'Home Wins': 2.26, 'Draw': 3.25,
     'Away Wins': 2.95, 'Away Team': 'Argentinos Juniors Reserve', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'River Plate', 'Commence Time': '16:00:00', 'Home Wins': 2.24, 'Draw': 3.2, 'Away Wins': 2.9,
     'Away Team': 'Argentinos', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'River Plate II', 'Commence Time': '16:00:00', 'Home Wins': 2.248, 'Draw': 3.24, 'Away Wins': 2.975,
     'Away Team': 'Argentinos Juniors II', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Aldosivi', 'Commence Time': '17:00:00', 'Home Wins': 2.55, 'Draw': 3.2, 'Away Wins': 2.5,
     'Away Team': 'Tigre', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.57, 'Draw': 3.2, 'Away Wins': 2.53,
     'Away Team': 'Tigre Reserve', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico', 'Commence Time': '17:00:00', 'Home Wins': 1.73, 'Draw': 3.55, 'Away Wins': 4.2,
     'Away Team': 'Patronato Res.', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman (Res)', 'Commence Time': '17:00:00', 'Home Wins': 1.66, 'Draw': 3.5,
     'Away Wins': 4.0, 'Away Team': 'CA Patronato (Res)', 'Bookmaker': 'Sportsbet', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.71, 'Draw': 3.55,
     'Away Wins': 4.22, 'Away Team': 'Patronato Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.73, 'Draw': 3.6,
     'Away Wins': 4.2, 'Away Team': 'CA Patronato Parana', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.74, 'Draw': 3.6,
     'Away Wins': 4.2, 'Away Team': 'CA Patronato Parana', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.74, 'Draw': 3.55,
     'Away Wins': 4.2, 'Away Team': 'CA Patronato Parana', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.75, 'Draw': 3.6,
     'Away Wins': 4.25, 'Away Team': 'CA Patronato Parana Reserve', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Atletico Tucuman Reserve', 'Commence Time': '17:00:00', 'Home Wins': 1.85, 'Draw': 3.6,
     'Away Wins': 3.4, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.54, 'Draw': 3.22, 'Away Wins': 2.5,
     'Away Team': 'CA Tigre Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.55, 'Draw': 3.2, 'Away Wins': 2.5,
     'Away Team': 'CA Tigre Reserve', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.6, 'Draw': 3.25, 'Away Wins': 2.6,
     'Away Team': 'CA TIGRE', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'CA Aldosivi Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.6, 'Draw': 3.25, 'Away Wins': 2.55,
     'Away Team': 'CA Tigre Reserve', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Colon Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.28, 'Draw': 3.1,
     'Away Wins': 2.95, 'Away Team': 'Estudiantes', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe II', 'Commence Time': '17:00:00', 'Home Wins': 2.245, 'Draw': 3.165,
     'Away Wins': 3.045, 'Away Team': 'Estudiantes II', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.26, 'Draw': 3.07,
     'Away Wins': 2.97, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.15,
     'Away Wins': 3.05, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.1,
     'Away Wins': 3.0, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.1,
     'Away Wins': 2.96, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Colon de Santa Fe Reserve', 'Commence Time': '17:00:00', 'Home Wins': 2.3, 'Draw': 3.1,
     'Away Wins': 2.95, 'Away Team': 'Estudiantes de LP Reserve', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.44, 'Draw': 3.1, 'Away Wins': 2.6,
     'Away Team': 'Montana 1921', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.45, 'Draw': 3.1, 'Away Wins': 2.65,
     'Away Team': 'PFC Montana 1921', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Maritsa', 'Commence Time': '17:00:00', 'Home Wins': 2.47, 'Draw': 3.15, 'Away Wins': 2.65,
     'Away Team': 'Montana', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.496, 'Draw': 3.2, 'Away Wins': 2.582,
     'Away Team': 'Montana', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Maritsa Plovdiv', 'Commence Time': '17:00:00', 'Home Wins': 2.55, 'Draw': 3.15, 'Away Wins': 2.7,
     'Away Team': 'PFC Montana 1921', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'FC Fakel Voronezh', 'Commence Time': '17:30:00', 'Home Wins': 3.1, 'Draw': 3.4, 'Away Wins': 2.15,
     'Away Team': 'PFK Krylia Sovetov Samara', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel', 'Commence Time': '17:30:00', 'Home Wins': 3.11, 'Draw': 3.51, 'Away Wins': 2.21,
     'Away Team': 'Kryliya Sovetov', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Voronezh', 'Commence Time': '17:30:00', 'Home Wins': 3.0, 'Draw': 3.35, 'Away Wins': 2.14,
     'Away Team': 'Krylia Sovetov Samara', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Voronezh', 'Commence Time': '17:30:00', 'Home Wins': 3.144, 'Draw': 3.64, 'Away Wins': 2.27,
     'Away Team': 'Krylia Sovetov', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Worenesch', 'Commence Time': '17:30:00', 'Home Wins': 2.45, 'Draw': 3.25, 'Away Wins': 2.55,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Worenesch', 'Commence Time': '17:30:00', 'Home Wins': 3.05, 'Draw': 3.4, 'Away Wins': 2.15,
     'Away Team': 'Kryliya Sovetov', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Fakel Worenesch', 'Commence Time': '17:30:00', 'Home Wins': 3.05, 'Draw': 3.4, 'Away Wins': 2.2,
     'Away Team': 'Kryliya Sovetov Samara', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'FC Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.62, 'Draw': 3.2, 'Away Wins': 2.5,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.2, 'Away Wins': 2.6,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.8, 'Draw': 3.3, 'Away Wins': 2.7,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.55, 'Draw': 2.95, 'Away Wins': 2.45,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Foxbet', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.15, 'Away Wins': 2.6,
     'Away Team': 'HJK', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.15, 'Away Wins': 2.65,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.7, 'Draw': 3.15, 'Away Wins': 2.67,
     'Away Team': 'HJK', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.71, 'Draw': 3.2, 'Away Wins': 2.61,
     'Away Team': 'HJK Helsinki', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Honka', 'Commence Time': '18:00:00', 'Home Wins': 2.71, 'Draw': 3.28, 'Away Wins': 2.57,
     'Away Team': 'HJK', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab Club', 'Commence Time': '18:00:00', 'Home Wins': 2.26, 'Draw': 3.096, 'Away Wins': 3.12,
     'Away Team': 'Shabab Al Ordon Al Quadisiya', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab Club', 'Commence Time': '18:00:00', 'Home Wins': 2.3, 'Draw': 3.06, 'Away Wins': 2.92,
     'Away Team': 'Shabab Al Ordun', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.3, 'Draw': 3.0, 'Away Wins': 3.0,
     'Away Team': 'Shabab Al-Ordon', 'Bookmaker': 'Palmerbet', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.34, 'Draw': 3.1, 'Away Wins': 2.95,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.35, 'Draw': 3.05, 'Away Wins': 3.05,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.35, 'Draw': 3.05, 'Away Wins': 2.92,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Sahab SC', 'Commence Time': '18:00:00', 'Home Wins': 2.35, 'Draw': 3.1, 'Away Wins': 3.0,
     'Away Team': 'Shabab AL Ordun', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat', 'Commence Time': '18:30:00', 'Home Wins': 1.47, 'Draw': 4.3, 'Away Wins': 5.4,
     'Away Team': 'Maccabi Girls Emek Hefer', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat (Women)', 'Commence Time': '18:30:00', 'Home Wins': 1.44, 'Draw': 4.4, 'Away Wins': 5.9,
     'Away Team': 'Maccabi Emek Hefer (Women)', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat SC', 'Commence Time': '18:30:00', 'Home Wins': 1.44, 'Draw': 4.1, 'Away Wins': 5.1,
     'Away Team': 'Maccabi Girls Emek Hefer', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Kiryat Gat SC', 'Commence Time': '18:30:00', 'Home Wins': 1.46, 'Draw': 4.2, 'Away Wins': 5.2,
     'Away Team': 'Maccabi Girls Emek Hefer', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich', 'Commence Time': '20:00:00', 'Home Wins': 1.17, 'Draw': 6.4, 'Away Wins': 13.0,
     'Away Team': 'Real Sociedad San Sebastian', 'Bookmaker': 'Odibet', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich', 'Commence Time': '20:00:00', 'Home Wins': 1.19, 'Draw': 6.3, 'Away Wins': 12.0,
     'Away Team': 'Real Sociedad San Sebastian', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich (W)', 'Commence Time': '20:00:00', 'Home Wins': 1.16, 'Draw': 6.7, 'Away Wins': 13.0,
     'Away Team': 'Real Sociedad (W)', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich W', 'Commence Time': '20:00:00', 'Home Wins': 1.14, 'Draw': 6.68, 'Away Wins': 13.36,
     'Away Team': 'Real Sociedad W', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'Bayern Munich W', 'Commence Time': '20:00:00', 'Home Wins': 1.18, 'Draw': 6.5, 'Away Wins': 13.0,
     'Away Team': 'Real Sociedad San Sebastian', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Everton', 'Commence Time': '20:30:00', 'Home Wins': 1.43, 'Draw': 4.4, 'Away Wins': 5.8,
     'Away Team': 'Leicester City WFC', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'Everton (W)', 'Commence Time': '20:30:00', 'Home Wins': 1.45, 'Draw': 4.5, 'Away Wins': 6.0,
     'Away Team': 'Leicester (W)', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'Everton FC', 'Commence Time': '20:30:00', 'Home Wins': 1.42, 'Draw': 4.3, 'Away Wins': 5.6,
     'Away Team': 'Leicester City Ladies', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'},
    {'Home Team': 'Everton FC', 'Commence Time': '20:30:00', 'Home Wins': 1.43, 'Draw': 4.4, 'Away Wins': 5.7,
     'Away Team': 'Leicester City WFC', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.3, 'Draw': 3.11, 'Away Wins': 2.08,
     'Away Team': 'Jazeera Amman', 'Bookmaker': 'Sportpesa', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.35, 'Draw': 3.15, 'Away Wins': 2.12,
     'Away Team': 'Al Jazeera Jordan', 'Bookmaker': 'Betika', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.35, 'Draw': 3.2, 'Away Wins': 2.15,
     'Away Team': 'Al Jazeera Club Jordan', 'Bookmaker': 'Betkings', 'Date': '29-09-2022'},
    {'Home Team': 'FC Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.4, 'Draw': 3.2, 'Away Wins': 2.15,
     'Away Team': 'AL Jazeera Club Amman', 'Bookmaker': 'Sportybet', 'Date': '29-09-2022'},
    {'Home Team': 'Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.24, 'Draw': 3.32, 'Away Wins': 2.098,
     'Away Team': 'Al-Jazeera Amman', 'Bookmaker': 'Xbet', 'Date': '29-09-2022'},
    {'Home Team': 'Maan', 'Commence Time': '20:30:00', 'Home Wins': 3.3, 'Draw': 3.1, 'Away Wins': 2.1,
     'Away Team': 'AL Jazeera Club Amman', 'Bookmaker': 'Bet9ja', 'Date': '29-09-2022'}
]

# TODO Get the total number of different times
times_list = []
for match in sorted_matches_list:
    commence_time = match['Commence Time']
    if commence_time not in times_list:
        times_list.append(commence_time)

# print(len(times_list))  # 12
# print("")
# for time in times_list:
#     print(time)

# TODO Group the matches by time. Should achieve 12 different groups
sorted_by_time_dict = {}
sorted_by_time_list = []
count, total = 0, 0
for match in sorted_matches_list:
    try:
        commence_time = match['Commence Time']
        # print(commence_time)
        next_commence_time = sorted_matches_list[sorted_matches_list.index(match) + 1]['Commence Time']
        sorted_by_time_list.append(match)
    except IndexError:
        sorted_by_time_list.append(match)
        # print(len(sorted_by_time_list))
        sorted_by_time_dict[commence_time] = sorted_by_time_list
        total += len(sorted_by_time_list)
        # print("")
        # print(total)
    else:
        # TODO Check whether the time is the same
        if commence_time != next_commence_time:
            sorted_by_time_dict[commence_time] = sorted_by_time_list

            #####################################################################################################
            sorted_by_teams_list = []
            # TODO Now sort by team
            for current_match in sorted_by_time_list:
                try:
                    next_match = sorted_matches_list[sorted_matches_list.index(match) + 1]['Commence Time']
                    previous_match = sorted_matches_list[sorted_matches_list.index(match) - 1]['Commence Time']

                    current_home_team = current_match['Home Team']
                    current_commence_time = current_match['Commence Time']
                    current_away_team = current_match['Away Team']
                    current_bookmaker = current_match['Bookmaker']

                    next_home_team = next_match['Home Team']
                    next_commence_time = next_match['Commence Time']
                    next_away_team = next_match['Away Team']
                    next_bookmaker = next_match['Bookmaker']

                    previous_home_team = previous_match['Home Team']
                    previous_commence_time = previous_match['Commence Time']
                    previous_away_team = previous_match['Away Team']
                    previous_bookmaker = previous_match['Bookmaker']

                    sorted_by_teams_list.append(current_match)
                except IndexError:
                    print("This is the end of the list")
                else:
                    # TODO Check if bookmaker is the same
                    if current_bookmaker != next_bookmaker:
                        # TODO Check








            #######################################################################################################

            # print(len(sorted_by_time_list))
            total += len(sorted_by_time_list)
            # print("")
            sorted_by_time_list = []


sorted_by_team_names = []
for current_match in sorted_matches_list:
    try:
        next_match= sorted_matches_list[sorted_matches_list.index(match) + 1]['Commence Time']
        previous_match = sorted_matches_list[sorted_matches_list.index(match) - 1]['Commence Time']

        current_home_team = current_match['Home Team']
        current_commence_time = current_match['Commence Time']
        current_away_team = current_match['Away Team']
        current_bookmaker = current_match['Bookmaker']

        next_home_team = next_match['Home Team']
        next_commence_time = next_match['Commence Time']
        next_away_team = next_match['Away Team']
        next_bookmaker = next_match['Bookmaker']

        previous_home_team = previous_match['Home Team']
        previous_commence_time = previous_match['Commence Time']
        previous_away_team = previous_match['Away Team']
        previous_bookmaker = previous_match['Bookmaker']

        sorted_by_team_names.append(current_match)
    except IndexError:
        print("This is the end of the list")
    else:

