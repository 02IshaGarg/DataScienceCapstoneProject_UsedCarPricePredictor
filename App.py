import streamlit as st
import pickle
import numpy as np
import pandas as pd

Model = pickle.load(open('CarDetailsbr.pkl','rb'))

# streamlit Part
st.title('Used Car Price Predictor 🚗')
st.markdown('Are you planning to sell your car?')
st.markdown("So let's try evaluating the price 💰")

# Car Brand
brand = st.selectbox('Select Car Brand',
                    ('Ambassador', 'Audi', 'BMW', 'Chevrolet', 'Daewoo', 'Datsun', 'Fiat', 'Force', 'Ford','Honda', 'Hyundai', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Land', 'MG', 'Mahindra', 'Maruti', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'OpelCorsa', 'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo'))

# car name
if brand == 'Chevrolet':
    name = st.selectbox('Select Car Model Number',
            ('Chevrolet Aveo 1.4', 'Chevrolet Aveo 1.4 CNG', 'Chevrolet Aveo 1.4 LS', 'Chevrolet Aveo 1.4 LT BSIV', 'Chevrolet Aveo 1.6 LT', 'Chevrolet Aveo 1.6 LT with ABS', 'Chevrolet Aveo U-VA 1.2', 'Chevrolet Aveo U-VA 1.2 LS', 'Chevrolet Aveo U-VA 1.2 LT', 'Chevrolet Aveo U-VA 1.2 LT WO ABS Airbag', 'Chevrolet Beat Diesel', 'Chevrolet Beat Diesel LS', 'Chevrolet Beat Diesel LT', 'Chevrolet Beat Diesel LT Option', 'Chevrolet Beat Diesel PS', 'Chevrolet Beat LS', 'Chevrolet Beat LT', 'Chevrolet Beat LT LPG', 'Chevrolet Beat LT Option', 'Chevrolet Beat PS', 'Chevrolet Captiva 2.0L VCDi', 'Chevrolet Captiva LT', 'Chevrolet Cruze LT', 'Chevrolet Cruze LTZ', 'Chevrolet Cruze LTZ AT', 'Chevrolet Enjoy 1.3 TCDi LS 8', 'Chevrolet Enjoy TCDi LS 8 Seater', 'Chevrolet Enjoy TCDi LT 7 Seater', 'Chevrolet Enjoy TCDi LT 8 Seater', 'Chevrolet Enjoy TCDi LTZ 7 Seater', 'Chevrolet Optra 1.6', 'Chevrolet Optra 1.6 LS', 'Chevrolet Optra Magnum 2.0 LS', 'Chevrolet Optra Magnum 2.0 LS BSIII', 'Chevrolet Optra Magnum 2.0 LT', 'Chevrolet Sail 1.2 Base', 'Chevrolet Sail 1.2 LT ABS', 'Chevrolet Sail 1.3 LS', 'Chevrolet Sail Hatchback 1.2 LS', 'Chevrolet Sail Hatchback 1.3 TCDi', 'Chevrolet Sail Hatchback 1.3 TCDi LT ABS', 'Chevrolet Sail Hatchback LS ABS', 'Chevrolet Sail Hatchback LT ABS', 'Chevrolet Sail LS ABS', 'Chevrolet Spark 1.0', 'Chevrolet Spark 1.0 LS', 'Chevrolet Spark 1.0 LT', 'Chevrolet Spark 1.0 LT BS3', 'Chevrolet Spark 1.0 LT Option Pack w/ Airbag', 'Chevrolet Spark 1.0 PS', 'Chevrolet Tavera LS B3 7 Seats BSII', 'Chevrolet Tavera LT L1 7 Seats BSIII', 'Chevrolet Tavera Neo 2 LS B4 7 Str BSIII', 'Chevrolet Tavera Neo 2 LT L 9 Str', 'Chevrolet Tavera Neo 3 10 Seats BSIV','Chevrolet Tavera Neo 3 9 Str BSIII', 'Chevrolet Tavera Neo 3 LS 7 C BSIII', 'Chevrolet Tavera Neo 3 LT 9 Seats BSIII', 'Chevrolet Tavera Neo 3 Max 9 Str BSIII', 'Chevrolet Tavera Neo LS B3 - 7(C) seats BSIII'))

elif brand == 'Ford':
    name = st.selectbox('Select Car Model Number',
            ('Ford Aspire Titanium BSIV', 'Ford Aspire Titanium Diesel BSIV', 'Ford Aspire Titanium Plus BSIV', 'Ford Aspire Titanium Plus Diesel BSIV','Ford Classic 1.4 Duratorq LXI', 'Ford Classic 1.6 Duratec LXI', 'Ford EcoSport 1.5 Diesel Ambiente BSIV', 'Ford EcoSport 1.5 Diesel Titanium BSIV', 'Ford EcoSport 1.5 Diesel Titanium Plus BSIV', 'Ford EcoSport 1.5 Diesel Trend BSIV', 'Ford EcoSport 1.5 Diesel Trend Plus BSIV', 'Ford EcoSport 1.5 Petrol Titanium BSIV', 'Ford EcoSport 1.5 Petrol Titanium Plus AT BSIV','Ford EcoSport 1.5 TDCi Titanium BSIV', 'Ford EcoSport 1.5 TDCi Titanium Plus BE BSIV', 'Ford EcoSport 1.5 TDCi Titanium Plus BSIV', 'Ford EcoSport 1.5 Ti VCT MT Titanium BE BSIV', 'Ford EcoSport 1.5 Ti VCT MT Titanium BSIV', 'Ford EcoSport 1.5 Ti VCT MT Trend BSIV', 'Ford Ecosport 1.0 Ecoboost Platinum Edition BSIV', 'Ford Ecosport 1.0 Ecoboost Titanium', 'Ford Ecosport 1.0 Ecoboost Titanium Optional', 'Ford Ecosport 1.5 DV5 MT Ambiente', 'Ford Ecosport 1.5 DV5 MT Titanium', 'Ford Ecosport 1.5 DV5 MT Titanium Optional', 'Ford Ecosport 1.5 DV5 MT Trend', 'Ford Ecosport 1.5 Diesel Titanium', 'Ford Ecosport 1.5 Diesel Titanium Plus', 'Ford Ecosport 1.5 Petrol Ambiente', 'Ford Ecosport 1.5 Petrol Titanium Plus', 'Ford Ecosport 1.5 Petrol Titanium Plus AT', 'Ford Ecosport 1.5 Petrol Trend', 'Ford Ecosport 1.5 Ti VCT AT Titanium', 'Ford Ecosport Sports Petrol', 'Ford Ecosport Thunder Edition Diesel', 'Ford Endeavour 2.2 Titanium AT 4X2', 'Ford Endeavour 2.5L 4X2','Ford Endeavour 2.5L 4X2 MT', 'Ford Endeavour 3.0L 4X4 AT', 'Ford Endeavour 3.2 Titanium AT 4X4', 'Ford Endeavour 4x2 XLT', 'Ford Endeavour 4x4 XLT', 'Ford Endeavour Hurricane Limited Edition', 'Ford Endeavour Titanium 4X2', 'Ford Endeavour Titanium Plus 4X4','Ford Endeavour XLT TDCi 4X2', 'Ford Fiesta 1.4 Duratec ZXI', 'Ford Fiesta 1.4 SXi TDCi', 'Ford Fiesta 1.4 SXi TDCi ABS', 'Ford Fiesta 1.4 ZXi Duratec', 'Ford Fiesta 1.4 ZXi Leather', 'Ford Fiesta 1.4 ZXi TDCi ABS', 'Ford Fiesta 1.5 TDCi Ambiente', 'Ford Fiesta 1.5 TDCi Titanium', 'Ford Fiesta 1.6 Duratec EXI Ltd', 'Ford Fiesta 1.6 Duratec S', 'Ford Fiesta 1.6 ZXi Duratec', 'Ford Fiesta 1.6 ZXi Leather', 'Ford Fiesta Classic 1.4 Duratorq CLXI', 'Ford Fiesta Classic 1.4 SXI Duratorq','Ford Fiesta Classic 1.6 Duratec CLXI', 'Ford Fiesta Diesel Style', 'Ford Fiesta Diesel Trend', 'Ford Fiesta Petrol Trend', 'Ford Fiesta Titanium 1.5 TDCi', 'Ford Figo 1.2P Ambiente MT', 'Ford Figo 1.2P Titanium MT', 'Ford Figo 1.2P Titanium Plus MT', 'Ford Figo 1.5 Sports Edition MT', 'Ford Figo 1.5D Ambiente ABS MT', 'Ford Figo 1.5D Titanium MT', 'Ford Figo 1.5D Titanium Opt MT', 'Ford Figo 1.5D Trend MT', 'Ford Figo 1.5P Titanium AT', 'Ford Figo Aspire 1.2 Ti-VCT Titanium Plus', 'Ford Figo Aspire 1.2 Ti-VCT Trend', 'Ford Figo Aspire 1.5 TDCi Ambiente ABS', 'Ford Figo Aspire 1.5 TDCi Titanium', 'Ford Figo Aspire 1.5 TDCi Titanium Plus', 'Ford Figo Aspire 1.5 TDCi Trend', 'Ford Figo Aspire 1.5 Ti-VCT Titanium', 'Ford Figo Aspire Facelift', 'Ford Figo Aspire Titanium Plus Diesel', 'Ford Figo Diesel Celebration Edition', 'Ford Figo Diesel EXI', 'Ford Figo Diesel LXI', 'Ford Figo Diesel Titanium', 'Ford Figo Diesel ZXI', 'Ford Figo Petrol EXI', 'Ford Figo Petrol LXI', 'Ford Figo Petrol Titanium','Ford Figo Petrol ZXI', 'Ford Figo Titanium', 'Ford Figo Titanium Diesel BSIV', 'Ford Figo Trend', 'Ford Freestyle Titanium', 'Ford Freestyle Titanium Diesel', 'Ford Freestyle Titanium Diesel BSIV', 'Ford Freestyle Titanium Plus', 'Ford Freestyle Titanium Plus Diesel', 'Ford Freestyle Titanium Plus Diesel BSIV', 'Ford Freestyle Trend Petrol BSIV', 'Ford Fusion 1.6 Duratec Petrol', 'Ford Ikon 1.3 Flair', 'Ford Ikon 1.3L Rocam Flair', 'Ford Ikon 1.4 TDCi DuraTorq', 'Ford Ikon 1.4 ZXi', 'Ford Ikon 1.6 ZXI NXt', 'Ford Ikon 1.8 D'))

elif brand == 'Honda':
    name = st.selectbox('Select Car Model',
            ('Honda Accord 2.4 AT', 'Honda Accord 2.4 MT', 'Honda Accord VTi-L (MT)', 'Honda Amaze E i-DTEC', 'Honda Amaze E i-Dtech', 'Honda Amaze E i-VTEC', 'Honda Amaze E i-Vtech', 'Honda Amaze EX i-Dtech', 'Honda Amaze S AT i-Vtech', 'Honda Amaze S CVT Petrol', 'Honda Amaze S Diesel', 'Honda Amaze S Petrol BSIV', 'Honda Amaze S i-DTEC', 'Honda Amaze S i-Dtech', 'Honda Amaze S i-VTEC', 'Honda Amaze S i-Vtech', 'Honda Amaze SX i-VTEC', 'Honda Amaze V CVT Petrol BSIV', 'Honda Amaze V Diesel BSIV', 'Honda Amaze VX AT i-Vtech', 'Honda Amaze VX Diesel BSIV', 'Honda Amaze VX O iDTEC', 'Honda Amaze VX Petrol BSIV', 'Honda Amaze VX i-DTEC', 'Honda Amaze VX i-VTEC', 'Honda BR-V i-DTEC VX MT', 'Honda BR-V i-VTEC S MT', 'Honda BR-V i-VTEC VX MT', 'Honda BRV i-DTEC V MT', 'Honda BRV i-VTEC V MT', 'Honda Brio 1.2 E MT', 'Honda Brio 1.2 S MT', 'Honda Brio 1.2 S Option MT', 'Honda Brio 1.2 VX MT', 'Honda Brio E MT', 'Honda Brio Exclusive Edition', 'Honda Brio S MT', 'Honda Brio S Option AT', 'Honda Brio V MT', 'Honda Brio VX', 'Honda CR-V Diesel 4WD', 'Honda City 1.3 DX', 'Honda City 1.3 EXI', 'Honda City 1.5 E MT', 'Honda City 1.5 EXI', 'Honda City 1.5 EXI S', 'Honda City 1.5 GXI', 'Honda City 1.5 S MT', 'Honda City 1.5 V AT', 'Honda City 1.5 V AT Exclusive', 'Honda City 1.5 V Elegance', 'Honda City 1.5 V MT', 'Honda City Corporate Edition', 'Honda City E', 'Honda City Edge Edition Diesel SV', 'Honda City S', 'Honda City V AT', 'Honda City V MT', 'Honda City VTEC', 'Honda City VX CVT', 'Honda City VX MT', 'Honda City i DTEC E', 'Honda City i DTEC S', 'Honda City i DTEC SV', 'Honda City i DTEC V', 'Honda City i DTEC VX', 'Honda City i DTec SV', 'Honda City i DTec V', 'Honda City i VTEC S', 'Honda City i VTEC SV', 'Honda City i VTEC V', 'Honda City i VTEC VX', 'Honda City i-DTEC SV', 'Honda City i-DTEC V', 'Honda City i-DTEC VX', 'Honda City i-DTEC ZX', 'Honda City i-VTEC CVT VX', 'Honda City i-VTEC CVT ZX', 'Honda City i-VTEC SV', 'Honda City i-VTEC VX', 'Honda City i-VTEC ZX', 'Honda Civic 1.8 (E) MT', 'Honda Civic 1.8 MT Sport', 'Honda Civic 1.8 S AT', 'Honda Civic 1.8 S MT', 'Honda Civic 1.8 V AT', 'Honda Civic 1.8 V MT', 'Honda Jazz 1.2 S i VTEC', 'Honda Jazz 1.2 V i VTEC', 'Honda Jazz 1.2 VX i VTEC', 'Honda Jazz 1.5 E i DTEC', 'Honda Jazz 1.5 S i DTEC', 'Honda Jazz 1.5 SV i DTEC', 'Honda Jazz 1.5 V i DTEC', 'Honda Jazz 1.5 VX i DTEC', 'Honda Jazz S', 'Honda Jazz Select Edition', 'Honda Jazz Select Edition Active', 'Honda Jazz V', 'Honda Jazz VX', 'Honda Jazz VX CVT', 'Honda Mobilio E i DTEC', 'Honda Mobilio S i DTEC', 'Honda Mobilio S i VTEC', 'Honda Mobilio V i DTEC', 'Honda Mobilio V i VTEC','Honda WR-V i-DTEC V', 'Honda WR-V i-DTEC VX', 'Honda WR-V i-VTEC VX'))

elif brand == 'Hyundai':
    name = st.selectbox('Select Car Model Number',
            ('Hyundai Accent CRDi', 'Hyundai Accent Executive', 'Hyundai Accent Executive CNG', 'Hyundai Accent GLE', 'Hyundai Accent GLE 1', 'Hyundai Accent GLE CNG', 'Hyundai Accent GLS', 'Hyundai Accent GLS 1.6 ABS', 'Hyundai Accent GLX', 'Hyundai Creta 1.4 CRDi Base', 'Hyundai Creta 1.4 CRDi S', 'Hyundai Creta 1.4 CRDi S Plus', 'Hyundai Creta 1.4 E Plus', 'Hyundai Creta 1.4 EX Diesel', 'Hyundai Creta 1.6 CRDi AT SX Plus', 'Hyundai Creta 1.6 CRDi SX', 'Hyundai Creta 1.6 CRDi SX Option', 'Hyundai Creta 1.6 CRDi SX Plus', 'Hyundai Creta 1.6 E Plus', 'Hyundai Creta 1.6 Gamma SX Plus', 'Hyundai Creta 1.6 SX', 'Hyundai Creta 1.6 SX Automatic', 'Hyundai Creta 1.6 SX Automatic Diesel', 'Hyundai Creta 1.6 SX Option', 'Hyundai Creta 1.6 VTVT AT SX Plus', 'Hyundai Creta 1.6 VTVT S', 'Hyundai EON 1.0 Era Plus', 'Hyundai EON 1.0 Kappa Magna Plus', 'Hyundai EON D Lite', 'Hyundai EON D Lite Plus', 'Hyundai EON Era', 'Hyundai EON Era Plus', 'Hyundai EON Era Plus Option', 'Hyundai EON Era Plus Sports Edition', 'Hyundai EON LPG Magna Plus', 'Hyundai EON Magna', 'Hyundai EON Magna Optional', 'Hyundai EON Magna Plus', 'Hyundai EON Magna Plus Option', 'Hyundai EON Sportz', 'Hyundai Elantra 2.0 SX AT', 'Hyundai Elantra CRDi (Leather Option)', 'Hyundai Elantra CRDi S', 'Hyundai Elantra CRDi SX', 'Hyundai Elantra SX', 'Hyundai Elite i20 Asta Option BSIV', 'Hyundai Elite i20 Asta Option CVT BSIV', 'Hyundai Elite i20 Diesel Asta Option', 'Hyundai Elite i20 Diesel Era', 'Hyundai Elite i20 Magna Plus BSIV', 'Hyundai Elite i20 Magna Plus Diesel', 'Hyundai Elite i20 Petrol Asta Option', 'Hyundai Elite i20 Petrol Magna Exective', 'Hyundai Elite i20 Sportz Plus BSIV', 'Hyundai Elite i20 Sportz Plus CVT BSIV', 'Hyundai Elite i20 Sportz Plus Dual Tone BSIV', 'Hyundai Getz 1.3 GLS', 'Hyundai Getz 1.3 GVS', 'Hyundai Getz 1.5 CRDi GVS', 'Hyundai Getz GL', 'Hyundai Getz GLE', 'Hyundai Getz GLS', 'Hyundai Getz GLS ABS', 'Hyundai Getz GLX', 'Hyundai Grand i10 1.2 CRDi Asta', 'Hyundai Grand i10 1.2 CRDi Magna', 'Hyundai Grand i10 1.2 CRDi Sportz Option', 'Hyundai Grand i10 1.2 Kappa Asta', 'Hyundai Grand i10 1.2 Kappa Era', 'Hyundai Grand i10 1.2 Kappa Magna AT', 'Hyundai Grand i10 1.2 Kappa Magna BSIV', 'Hyundai Grand i10 1.2 Kappa Sportz AT', 'Hyundai Grand i10 1.2 Kappa Sportz BSIV', 'Hyundai Grand i10 1.2 Kappa Sportz Dual Tone', 'Hyundai Grand i10 1.2 Kappa Sportz Option','Hyundai Grand i10 AT Asta', 'Hyundai Grand i10 Asta', 'Hyundai Grand i10 Asta Option', 'Hyundai Grand i10 Asta Option AT', 'Hyundai Grand i10 CRDi Asta', 'Hyundai Grand i10 CRDi Asta Option', 'Hyundai Grand i10 CRDi Magna', 'Hyundai Grand i10 CRDi Sportz', 'Hyundai Grand i10 Magna', 'Hyundai Grand i10 Magna AT', 'Hyundai Grand i10 Nios AMT Magna', 'Hyundai Grand i10 Nios Magna CRDi', 'Hyundai Grand i10 Nios Sportz', 'Hyundai Grand i10 Sportz', 'Hyundai Santa Fe 4WD AT', 'Hyundai Santa Fe 4X4', 'Hyundai Santro AT', 'Hyundai Santro AT CNG', 'Hyundai Santro Asta', 'Hyundai Santro Era', 'Hyundai Santro GLS I - Euro I', 'Hyundai Santro GLS I - Euro II', 'Hyundai Santro GS', 'Hyundai Santro LE', 'Hyundai Santro LE zipPlus', 'Hyundai Santro LP zipPlus', 'Hyundai Santro LS zipPlus', 'Hyundai Santro Magna AMT BSIV', 'Hyundai Santro Magna BSIV', 'Hyundai Santro Magna CNG BSIV', 'Hyundai Santro Sportz AMT', 'Hyundai Santro Sportz BSIV', 'Hyundai Santro Xing GL', 'Hyundai Santro Xing GL PLUS CNG', 'Hyundai Santro Xing GL Plus', 'Hyundai Santro Xing GL Plus LPG', 'Hyundai Santro Xing GLS', 'Hyundai Santro Xing GLS Audio LPG', 'Hyundai Santro Xing GLS CNG', 'Hyundai Santro Xing XG', 'Hyundai Santro Xing XG AT', 'Hyundai Santro Xing XG eRLX Euro III', 'Hyundai Santro Xing XK', 'Hyundai Santro Xing XK (Non-AC)', 'Hyundai Santro Xing XK eRLX EuroIII', 'Hyundai Santro Xing XL AT eRLX Euro III', 'Hyundai Santro Xing XL eRLX Euro III', 'Hyundai Santro Xing XO', 'Hyundai Santro Xing XS', 'Hyundai Santro Xing XS eRLX Euro III', 'Hyundai Sonata 2.4L AT', 'Hyundai Sonata AT Leather', 'Hyundai Sonata CRDi M/T', 'Hyundai Tucson 2.0 e-VGT 2WD AT GL', 'Hyundai Tucson 2.0 e-VGT 2WD MT', 'Hyundai Tucson CRDi', 'Hyundai Venue SX Opt Diesel', 'Hyundai Venue SX Opt Turbo BSIV', 'Hyundai Verna 1.4 CRDi', 'Hyundai Verna 1.4 EX', 'Hyundai Verna 1.4 VTVT', 'Hyundai Verna 1.6 CRDI', 'Hyundai Verna 1.6 CRDI SX Option', 'Hyundai Verna 1.6 CRDi AT SX', 'Hyundai Verna 1.6 CRDi SX', 'Hyundai Verna 1.6 SX', 'Hyundai Verna 1.6 SX CRDi (O)', 'Hyundai Verna 1.6 SX VTVT', 'Hyundai Verna 1.6 SX VTVT (O)', 'Hyundai Verna 1.6 SX VTVT AT', 'Hyundai Verna 1.6 VTVT', 'Hyundai Verna 1.6 VTVT AT S Option', 'Hyundai Verna 1.6 VTVT S', 'Hyundai Verna 1.6 VTVT SX', 'Hyundai Verna 1.6 Xi ABS', 'Hyundai Verna 1.6 i ABS', 'Hyundai Verna CRDi', 'Hyundai Verna CRDi 1.6 AT EX', 'Hyundai Verna CRDi 1.6 AT SX Option', 'Hyundai Verna CRDi 1.6 EX', 'Hyundai Verna CRDi 1.6 SX', 'Hyundai Verna CRDi 1.6 SX Option', 'Hyundai Verna CRDi ABS', 'Hyundai Verna CRDi SX', 'Hyundai Verna CRDi SX ABS', 'Hyundai Verna SX', 'Hyundai Verna SX AT Diesel', 'Hyundai Verna SX CRDi AT', 'Hyundai Verna SX Diesel', 'Hyundai Verna Transform CRDi VGT ABS', 'Hyundai Verna Transform CRDi VGT SX ABS', 'Hyundai Verna Transform SX VTVT', 'Hyundai Verna Transform VTVT', 'Hyundai Verna VTVT 1.6 AT SX Option', 'Hyundai Verna VTVT 1.6 SX', 'Hyundai Verna XXi (Petrol)', 'Hyundai Verna i (Petrol)', 'Hyundai Xcent 1.1 CRDi Base', 'Hyundai Xcent 1.1 CRDi S', 'Hyundai Xcent 1.1 CRDi SX', 'Hyundai Xcent 1.1 CRDi SX Option', 'Hyundai Xcent 1.2 CRDi E', 'Hyundai Xcent 1.2 CRDi S', 'Hyundai Xcent 1.2 CRDi SX', 'Hyundai Xcent 1.2 Kappa Base', 'Hyundai Xcent 1.2 Kappa S', 'Hyundai Xcent 1.2 Kappa SX', 'Hyundai Xcent 1.2 VTVT E Plus', 'Hyundai Xcent 1.2 VTVT S', 'Hyundai Xcent 1.2 VTVT S AT', 'Hyundai i10 Asta AT', 'Hyundai i10 Era', 'Hyundai i10 Era 1.1', 'Hyundai i10 Era 1.1 iTech SE', 'Hyundai i10 Magna', 'Hyundai i10 Magna 1.1', 'Hyundai i10 Magna 1.1 iTech SE', 'Hyundai i10 Magna 1.1L', 'Hyundai i10 Magna 1.2', 'Hyundai i10 Magna 1.2 iTech SE', 'Hyundai i10 Magna LPG', 'Hyundai i10 Sportz', 'Hyundai i10 Sportz 1.1L', 'Hyundai i10 Sportz 1.2', 'Hyundai i10 Sportz 1.2 AT', 'Hyundai i10 Sportz AT', 'Hyundai i20 1.2 Asta', 'Hyundai i20 1.2 Asta Dual Tone', 'Hyundai i20 1.2 Asta Option', 'Hyundai i20 1.2 Era', 'Hyundai i20 1.2 Magna', 'Hyundai i20 1.2 Magna Executive', 'Hyundai i20 1.2 Sportz', 'Hyundai i20 1.2 Spotz', 'Hyundai i20 1.4 Asta Option', 'Hyundai i20 1.4 CRDi Asta', 'Hyundai i20 1.4 CRDi Era', 'Hyundai i20 1.4 CRDi Magna', 'Hyundai i20 1.4 CRDi Sportz', 'Hyundai i20 1.4 Magna ABS', 'Hyundai i20 1.4 Magna Executive', 'Hyundai i20 1.4 Sportz', 'Hyundai i20 2015-2017 Magna 1.2', 'Hyundai i20 2015-2017 Sportz Option 1.4 CRDi', 'Hyundai i20 Active 1.2 S', 'Hyundai i20 Active 1.2 SX', 'Hyundai i20 Active 1.4 SX', 'Hyundai i20 Active 1.4 SX with AVN', 'Hyundai i20 Active S Diesel', 'Hyundai i20 Active S Petrol', 'Hyundai i20 Active SX Petrol', 'Hyundai i20 Asta', 'Hyundai i20 Asta (o)', 'Hyundai i20 Asta (o) 1.4 CRDi (Diesel)', 'Hyundai i20 Asta 1.2', 'Hyundai i20 Asta 1.4 CRDi', 'Hyundai i20 Asta 1.4 CRDi (Diesel)', 'Hyundai i20 Asta Option 1.2', 'Hyundai i20 Asta Option 1.4 CRDi', 'Hyundai i20 Magna', 'Hyundai i20 Magna 1.2', 'Hyundai i20 Magna 1.4 CRDi', 'Hyundai i20 Magna 1.4 CRDi (Diesel)', 'Hyundai i20 Magna Optional 1.2', 'Hyundai i20 Magna Optional 1.4 CRDi', 'Hyundai i20 Sportz 1.2', 'Hyundai i20 Sportz 1.4 CRDi', 'Hyundai i20 Sportz Option 1.2', 'Hyundai i20 Sportz Petrol'))

elif brand == 'Mahindra':
    name = st.selectbox('Select Car Model Number',
            ('Mahindra Alturas G4 4X2 AT BSIV', 'Mahindra Bolero 2011-2019 SLE', 'Mahindra Bolero 2011-2019 SLX', 'Mahindra Bolero 2011-2019 SLX 2WD BSIII', 'Mahindra Bolero B4', 'Mahindra Bolero B6', 'Mahindra Bolero DI', 'Mahindra Bolero DI DX 7 Seater', 'Mahindra Bolero DI DX 8 Seater', 'Mahindra Bolero Power Plus LX', 'Mahindra Bolero Power Plus Plus AC BSIV PS', 'Mahindra Bolero Power Plus Plus Non AC BSIV PS', 'Mahindra Bolero Power Plus SLE', 'Mahindra Bolero Power Plus SLX', 'Mahindra Bolero Power Plus ZLX', 'Mahindra Bolero SLE', 'Mahindra Bolero SLE BSIII', 'Mahindra Bolero SLX', 'Mahindra Bolero SLX 2WD', 'Mahindra Bolero SLX 2WD BSIII', 'Mahindra Bolero SLX 4WD BSIII', 'Mahindra Ingenio CRDe', 'Mahindra Jeep CJ 500 DI', 'Mahindra Jeep CL 500 MDI', 'Mahindra Jeep Classic', 'Mahindra Jeep MM 540', 'Mahindra Jeep MM 550 XDB', 'Mahindra Jeep MM 775 XDB', 'Mahindra KUV 100 D75 K2', 'Mahindra KUV 100 D75 K4 Plus 5Str', 'Mahindra KUV 100 D75 K6 Plus', 'Mahindra KUV 100 G80 K2', 'Mahindra KUV 100 G80 K4 Plus', 'Mahindra KUV 100 mFALCON D75 K6', 'Mahindra KUV 100 mFALCON D75 K8', 'Mahindra KUV 100 mFALCON D75 K8 AW', 'Mahindra KUV 100 mFALCON G80 K2', 'Mahindra KUV 100 mFALCON G80 K2 Plus', 'Mahindra KUV 100 mFALCON G80 K8 5str', 'Mahindra Marazzo M2 8Str', 'Mahindra Marazzo M4', 'Mahindra Marazzo M8 8Str', 'Mahindra NuvoSport N8', 'Mahindra Quanto C4', 'Mahindra Quanto C6', 'Mahindra Quanto C8', 'Mahindra Renault Logan 1.4 GLX Petrol', 'Mahindra Renault Logan 1.5 DLE Diesel', 'Mahindra Renault Logan 1.5 DLS', 'Mahindra Renault Logan 1.5 DLX Diesel', 'Mahindra Renault Logan 1.6 Petrol GLSX', 'Mahindra Scorpio 1.99 S10', 'Mahindra Scorpio 1.99 S4', 'Mahindra Scorpio 1.99 S6 Plus', 'Mahindra Scorpio 2.6 CRDe', 'Mahindra Scorpio 2.6 CRDe SLE', 'Mahindra Scorpio 2.6 SLX CRDe', 'Mahindra Scorpio 2.6 SLX Turbo 7 Seater', 'Mahindra Scorpio 2.6 Turbo 7 Str', 'Mahindra Scorpio 2.6 Turbo 9 Str', 'Mahindra Scorpio BSIV', 'Mahindra Scorpio EX', 'Mahindra Scorpio LX', 'Mahindra Scorpio LX BSIV', 'Mahindra Scorpio M2DI', 'Mahindra Scorpio REV 116', 'Mahindra Scorpio S10 7 Seater', 'Mahindra Scorpio S11 BSIV', 'Mahindra Scorpio S2 7 Seater', 'Mahindra Scorpio S2 9 Seater', 'Mahindra Scorpio S4 4WD', 'Mahindra Scorpio S5 BSIV', 'Mahindra Scorpio S6 Plus 7 Seater', 'Mahindra Scorpio S7 140 BSIV', 'Mahindra Scorpio S9 BSIV', 'Mahindra Scorpio SLE BS IV', 'Mahindra Scorpio SLE BS IV', 'Mahindra Scorpio SLE BSIII', 'Mahindra Scorpio SLE BSIV', 'Mahindra Scorpio SLX 2.6 Turbo 8 Str', 'Mahindra Scorpio VLS 2.2 mHawk', 'Mahindra Scorpio VLS AT 2.2 mHAWK', 'Mahindra Scorpio VLX 2.2 mHawk Airbag BSIV', 'Mahindra Scorpio VLX 2WD ABS AT BSIII', 'Mahindra Scorpio VLX 2WD AIRBAG BSIV', 'Mahindra Scorpio VLX 2WD AIRBAG SE BSIV', 'Mahindra Scorpio VLX 2WD AT BSIV', 'Mahindra Scorpio VLX 2WD BSIII', 'Mahindra Scorpio VLX 2WD BSIV', 'Mahindra Scorpio VLX AT 2WD BSIII', 'Mahindra Supro VX 8 Str', 'Mahindra TUV 300 Plus P4', 'Mahindra TUV 300 T10', 'Mahindra TUV 300 T10 Dual Tone', 'Mahindra TUV 300 T4', 'Mahindra TUV 300 T4 Plus', 'Mahindra TUV 300 T6 Plus', 'Mahindra TUV 300 T8', 'Mahindra TUV 300 T8 AMT', 'Mahindra TUV 300 mHAWK100 T8', 'Mahindra Thar 4X2', 'Mahindra Thar 4X4', 'Mahindra Thar CRDe', 'Mahindra Thar CRDe ABS', 'Mahindra Thar CRDe AC', 'Mahindra Thar DI 4X2', 'Mahindra Thar DI 4X4 PS', 'Mahindra Verito 1.5 D2 BSIII', 'Mahindra Verito 1.5 D2 BSIV', 'Mahindra Verito 1.5 D4 BSIV', 'Mahindra Verito 1.5 D6 BSIII', 'Mahindra Verito Vibe 1.5 dCi D4', 'Mahindra Verito Vibe 1.5 dCi D6', 'Mahindra XUV300 W8 Option', 'Mahindra XUV300 W8 Option Diesel BSIV', 'Mahindra XUV500 AT W10 1.99 mHawk', 'Mahindra XUV500 AT W10 AWD', 'Mahindra XUV500 AT W10 FWD', 'Mahindra XUV500 AT W6 2WD', 'Mahindra XUV500 AT W8 FWD', 'Mahindra XUV500 W10 1.99 mHawk', 'Mahindra XUV500 W10 2WD', 'Mahindra XUV500 W10 AWD', 'Mahindra XUV500 W11 AT BSIV', 'Mahindra XUV500 W11 Option AT AWD', 'Mahindra XUV500 W11 Option AWD', 'Mahindra XUV500 W5 BSIV', 'Mahindra XUV500 W6 1.99 mHawk', 'Mahindra XUV500 W6 2WD', 'Mahindra XUV500 W7', 'Mahindra XUV500 W7 AT BSIV', 'Mahindra XUV500 W7 BSIV', 'Mahindra XUV500 W8 2WD', 'Mahindra XUV500 W8 4WD', 'Mahindra Xylo Celebration Edition BSIV', 'Mahindra Xylo D2', 'Mahindra Xylo D2 BS IV', 'Mahindra Xylo D2 BSIV', 'Mahindra Xylo D2 Maxx', 'Mahindra Xylo D4', 'Mahindra Xylo D4 BSIV', 'Mahindra Xylo E4', 'Mahindra Xylo E4 8S', 'Mahindra Xylo E4 ABS BS IV', 'Mahindra Xylo E4 BS III', 'Mahindra Xylo E6', 'Mahindra Xylo E8', 'Mahindra Xylo E8 ABS Airbag BSIV', 'Mahindra Xylo E9', 'Mahindra Xylo H4', 'Mahindra Xylo H4 ABS', 'Mahindra Xylo H8 ABS with Airbags'))

elif brand == 'Maruti':
    name = st.selectbox('Select Car Model Number',
            ('Maruti 800 AC', 'Maruti 800 AC BSII', 'Maruti 800 AC BSIII', 'Maruti 800 AC Uniq', 'Maruti 800 DUO AC LPG','Maruti 800 DX', 'Maruti 800 EX', 'Maruti 800 Std', 'Maruti 800 Std BSII', 'Maruti 800 Std BSIII', 'Maruti 800 Std MPFi', 'Maruti A-Star AT VXI', 'Maruti A-Star Lxi', 'Maruti A-Star Vxi', 'Maruti Alto 800 Base', 'Maruti Alto 800 CNG LXI', 'Maruti Alto 800 CNG LXI Optional', 'Maruti Alto 800 LX', 'Maruti Alto 800 LXI', 'Maruti Alto 800 LXI Airbag', 'Maruti Alto 800 LXI CNG', 'Maruti Alto 800 LXI Opt BSIV', 'Maruti Alto 800 LXI Optional', 'Maruti Alto 800 Std Optional', 'Maruti Alto 800 VXI', 'Maruti Alto Green LXi (CNG)', 'Maruti Alto K10 2010-2014 VXI', 'Maruti Alto K10 LX', 'Maruti Alto K10 LXI', 'Maruti Alto K10 LXI CNG', 'Maruti Alto K10 LXI CNG Optional', 'Maruti Alto K10 VXI', 'Maruti Alto K10 VXI AGS', 'Maruti Alto K10 VXI AGS Optional', 'Maruti Alto K10 VXI Airbag', 'Maruti Alto K10 VXI Optional', 'Maruti Alto LX', 'Maruti Alto LX BSIII', 'Maruti Alto LXI', 'Maruti Alto LXi', 'Maruti Alto LXi BSII', 'Maruti Alto LXi BSIII', 'Maruti Alto STD', 'Maruti Alto VXi', 'Maruti Baleno Alpha', 'Maruti Baleno Alpha 1.2', 'Maruti Baleno Alpha 1.3', 'Maruti Baleno Alpha CVT', 'Maruti Baleno Delta 1.2', 'Maruti Baleno Delta 1.3', 'Maruti Baleno Delta Automatic', 'Maruti Baleno Delta Diesel', 'Maruti Baleno RS 1.0 Petrol', 'Maruti Baleno Sigma 1.2', 'Maruti Baleno Vxi', 'Maruti Baleno Zeta', 'Maruti Baleno Zeta 1.2', 'Maruti Baleno Zeta 1.3', 'Maruti Baleno Zeta Automatic', 'Maruti Celerio Green VXI', 'Maruti Celerio LXI MT BSIV', 'Maruti Celerio VDi', 'Maruti Celerio VXI','Maruti Celerio VXI AMT BSIV', 'Maruti Celerio VXI AT', 'Maruti Celerio VXI Optional', 'Maruti Celerio X ZXI BSIV', 'Maruti Celerio ZDi', 'Maruti Celerio ZXI', 'Maruti Celerio ZXI AMT BSIV', 'Maruti Celerio ZXI AT', 'Maruti Celerio ZXI MT BSIV', 'Maruti Celerio ZXI Optional AMT BSIV', 'Maruti Ciaz 1.3 Delta', 'Maruti Ciaz 1.4 AT Zeta', 'Maruti Ciaz 1.4 Alpha', 'Maruti Ciaz 1.4 Delta', 'Maruti Ciaz 1.4 Zeta', 'Maruti Ciaz S 1.3', 'Maruti Ciaz Sigma BSIV', 'Maruti Ciaz VDI SHVS', 'Maruti Ciaz VDi', 'Maruti Ciaz VDi Option SHVS','Maruti Ciaz VDi Plus', 'Maruti Ciaz VDi Plus SHVS', 'Maruti Ciaz VXi', 'Maruti Ciaz VXi Plus', 'Maruti Ciaz ZDi', 'Maruti Ciaz ZDi Plus', 'Maruti Ciaz ZDi Plus SHVS', 'Maruti Ciaz ZDi SHVS', 'Maruti Ciaz ZXi', 'Maruti Ciaz ZXi Plus', 'Maruti Ciaz Zeta BSIV', 'Maruti Eeco 5 STR With AC Plus HTR CNG', 'Maruti Eeco 5 Seater AC BSIV', 'Maruti Eeco 5 Seater Standard BSIV', 'Maruti Eeco 7 Seater Standard BSIV', 'Maruti Eeco CNG 5 Seater AC BSIV', 'Maruti Eeco Smiles 5 Seater AC', 'Maruti Ertiga 1.5 VDI', 'Maruti Ertiga BSIV VXI AT', 'Maruti Ertiga BSIV ZXI', 'Maruti Ertiga SHVS LDI', 'Maruti Ertiga SHVS LDI Option', 'Maruti Ertiga SHVS VDI', 'Maruti Ertiga SHVS ZDI', 'Maruti Ertiga SHVS ZDI Plus', 'Maruti Ertiga VDI', 'Maruti Ertiga VDI Limited Edition', 'Maruti Ertiga VXI', 'Maruti Ertiga VXI ABS', 'Maruti Ertiga VXI CNG', 'Maruti Ertiga VXI Petrol', 'Maruti Ertiga ZDI', 'Maruti Ertiga ZDI Plus', 'Maruti Ertiga ZXI', 'Maruti Ertiga ZXI AT Petrol', 'Maruti Esteem AX', 'Maruti Esteem Lxi','Maruti Esteem Lxi - BSIII', 'Maruti Esteem VX', 'Maruti Esteem Vxi', 'Maruti Esteem Vxi - BSIII', 'Maruti Estilo LXI', 'Maruti Grand Vitara MT', 'Maruti Gypsy E MG410W ST', 'Maruti Gypsy King HT BSIV', 'Maruti Gypsy King Hard Top', 'Maruti Gypsy King Hard Top Ambulance BSIV', 'Maruti Ignis 1.2 AMT Alpha BSIV', 'Maruti Ignis 1.2 AMT Delta BSIV', 'Maruti Ignis 1.2 Alpha BSIV', 'Maruti Ignis 1.2 Delta BSIV', 'Maruti Ignis 1.2 Sigma BSIV', 'Maruti Ignis 1.2 Zeta BSIV', 'Maruti Ignis 1.3 Delta', 'Maruti Omni 5 Str STD', 'Maruti Omni 5 Str STD LPG', 'Maruti Omni 8 Seater BSII', 'Maruti Omni 8 Seater BSIV', 'Maruti Omni BSIII 8-STR W/ IMMOBILISER', 'Maruti Omni CNG', 'Maruti Omni E 8 Str STD', 'Maruti Omni E MPI STD BS IV', 'Maruti Omni LPG CARGO BSIII W IMMOBILISER', 'Maruti Omni LPG STD BSIV', 'Maruti Omni MPI STD BSIV', 'Maruti Omni Maruti Omni MPI STD BSIII 5-STR W/ IMMOBILISER', 'Maruti Ritz LDi', 'Maruti Ritz LXI', 'Maruti Ritz LXi', 'Maruti Ritz VDI (ABS) BS IV', 'Maruti Ritz VDi', 'Maruti Ritz VXI', 'Maruti Ritz VXi', 'Maruti S-Cross Alpha DDiS 200 SH', 'Maruti S-Cross Delta DDiS 200 SH', 'Maruti S-Cross Facelift', 'Maruti S-Cross Sigma DDiS 200 SH', 'Maruti S-Cross Zeta DDiS 200 SH', 'Maruti S-Presso VXI Plus', 'Maruti SX4 Celebration Diesel', 'Maruti SX4 Celebration Petrol', 'Maruti SX4 S Cross DDiS 320 Delta', 'Maruti SX4 S Cross DDiS 320 Zeta', 'Maruti SX4 VDI', 'Maruti SX4 Vxi BSIII', 'Maruti SX4 Vxi BSIV', 'Maruti SX4 ZDI', 'Maruti SX4 ZDI Leather', 'Maruti SX4 ZXI AT', 'Maruti SX4 ZXI MT BSIV', 'Maruti SX4 Zxi BSIII', 'Maruti SX4 Zxi with Leather BSIII', 'Maruti Swift 1.2 DLX', 'Maruti Swift 1.3 DLX', 'Maruti Swift 1.3 LXI', 'Maruti Swift 1.3 VXI ABS', 'Maruti Swift 1.3 VXi', 'Maruti Swift AMT VXI', 'Maruti Swift DDiS LDI', 'Maruti Swift DDiS VDI','Maruti Swift Dzire 1.2 Vxi BSIV', 'Maruti Swift Dzire AMT VDI', 'Maruti Swift Dzire AMT VXI', 'Maruti Swift Dzire AMT ZXI', 'Maruti Swift Dzire AMT ZXI Plus BS IV', 'Maruti Swift Dzire LDI', 'Maruti Swift Dzire LDI Optional', 'Maruti Swift Dzire LDIX Limited Edition', 'Maruti Swift Dzire LDi', 'Maruti Swift Dzire LXI', 'Maruti Swift Dzire LXI Option', 'Maruti Swift Dzire LXi', 'Maruti Swift Dzire Tour LDI', 'Maruti Swift Dzire VDI', 'Maruti Swift Dzire VDI Optional', 'Maruti Swift Dzire VDi', 'Maruti Swift Dzire VXI', 'Maruti Swift Dzire VXI 1.2 BS IV', 'Maruti Swift Dzire VXi', 'Maruti Swift Dzire Vdi BSIV', 'Maruti Swift Dzire ZDI', 'Maruti Swift Dzire ZXI', 'Maruti Swift Dzire ZXI 1.2 BS IV', 'Maruti Swift Dzire ZXI Plus', 'Maruti Swift Glam', 'Maruti Swift LDI', 'Maruti Swift LDI BSIV', 'Maruti Swift LDI Optional', 'Maruti Swift LXI', 'Maruti Swift LXI Option', 'Maruti Swift LXi BSIV', 'Maruti Swift Ldi BSIII', 'Maruti Swift Ldi BSIV', 'Maruti Swift Star VDI', 'Maruti Swift VDI', 'Maruti Swift VDI BSIV', 'Maruti Swift VDI Optional', 'Maruti Swift VDi BSIII W/ ABS', 'Maruti Swift VVT VXI', 'Maruti Swift VVT ZXI', 'Maruti Swift VXI', 'Maruti Swift VXI BSIII', 'Maruti Swift VXI BSIV', 'Maruti Swift VXI Deca', 'Maruti Swift VXI Optional', 'Maruti Swift VXI with ABS', 'Maruti Swift VXi BSIV', 'Maruti Swift Vdi BSIII', 'Maruti Swift ZDI', 'Maruti Swift ZDI Plus', 'Maruti Swift ZDi', 'Maruti Swift ZDi BSIV', 'Maruti Swift ZXI', 'Maruti Swift ZXI ABS', 'Maruti Swift ZXI BSIV', 'Maruti Swift ZXI Plus', 'Maruti Swift ZXi BSIV', 'Maruti Vitara Brezza LDi', 'Maruti Vitara Brezza LDi Option', 'Maruti Vitara Brezza VDi', 'Maruti Vitara Brezza VDi Option', 'Maruti Vitara Brezza ZDi', 'Maruti Vitara Brezza ZDi Plus', 'Maruti Vitara Brezza ZDi Plus AMT', 'Maruti Vitara Brezza ZDi Plus AMT Dual Tone', 'Maruti Vitara Brezza ZDi Plus Dual Tone', 'Maruti Wagon R AMT VXI', 'Maruti Wagon R AMT VXI Option', 'Maruti Wagon R AX', 'Maruti Wagon R CNG LXI', 'Maruti Wagon R DUO LPG', 'Maruti Wagon R Duo Lxi', 'Maruti Wagon R LX', 'Maruti Wagon R LX BS IV', 'Maruti Wagon R LX BSIII', 'Maruti Wagon R LX Minor', 'Maruti Wagon R LXI', 'Maruti Wagon R LXI BS IV', 'Maruti Wagon R LXI BSIII', 'Maruti Wagon R LXI CNG', 'Maruti Wagon R LXI DUO BS IV', 'Maruti Wagon R LXI DUO BSIII', 'Maruti Wagon R LXI LPG BSIV', 'Maruti Wagon R LXI Minor', 'Maruti Wagon R Stingray LXI', 'Maruti Wagon R Stingray VXI', 'Maruti Wagon R VX', 'Maruti Wagon R VXI', 'Maruti Wagon R VXI AMT', 'Maruti Wagon R VXI AMT1.2BSIV', 'Maruti Wagon R VXI BS IV', 'Maruti Wagon R VXI BS IV with ABS', 'Maruti Wagon R VXI BSII', 'Maruti Wagon R VXI BSIII', 'Maruti Wagon R VXI Minor', 'Maruti Wagon R VXI Minor ABS', 'Maruti Wagon R VXI Optional', 'Maruti Wagon R VXI Plus Optional', 'Maruti Wagon R VXi BSII', 'Maruti Wagon R ZXI 1.2', 'Maruti Zen D', 'Maruti Zen D PS', 'Maruti Zen Estilo 1.1 LXI BSIII','Maruti Zen Estilo 1.1 VXI BSIII', 'Maruti Zen Estilo LX BSIII', 'Maruti Zen Estilo LX BSIV', 'Maruti Zen Estilo LXI BS IV', 'Maruti Zen Estilo LXI BSIII', 'Maruti Zen Estilo LXI Green (CNG)', 'Maruti Zen Estilo Sports', 'Maruti Zen Estilo VXI BSIII', 'Maruti Zen Estilo VXI BSIV', 'Maruti Zen LX', 'Maruti Zen LX - BS III', 'Maruti Zen LXI', 'Maruti Zen LXi - BS III', 'Maruti Zen LXi BSII', 'Maruti Zen VX', 'Maruti Zen VXI', 'Maruti Zen VXi - BS III'))

elif brand == 'Renault':
    name = st.selectbox('Select Car Model Number',
            ('Renault Captur 1.5 Diesel RXT', 'Renault Captur 1.5 Diesel RXT Mono', 'Renault Duster 110PS Diesel RxL','Renault Duster 110PS Diesel RxZ', 'Renault Duster 110PS Diesel RxZ AWD', 'Renault Duster 110PS Diesel RxZ Plus','Renault Duster 85PS Diesel RxE', 'Renault Duster 85PS Diesel RxL', 'Renault Duster 85PS Diesel RxL Optional', 'Renault Duster 85PS Diesel RxL Plus', 'Renault Duster 85PS Diesel RxZ', 'Renault Duster Petrol RxL', 'Renault Duster RXL AWD','Renault Fluence 1.5', 'Renault KWID 1.0', 'Renault KWID 1.0 RXL', 'Renault KWID 1.0 RXT Optional', 'Renault KWID AMT', 'Renault KWID Climber 1.0 AMT', 'Renault KWID Climber 1.0 AMT BSIV', 'Renault KWID Climber 1.0 MT Opt BSIV', 'Renault KWID RXE', 'Renault KWID RXL', 'Renault KWID RXL BSIV', 'Renault KWID RXT', 'Renault KWID RXT BSIV', 'Renault KWID RXT Optional', 'Renault Koleos 2.0 Diesel', 'Renault Lodgy 85PS RxL', 'Renault Lodgy Stepway 85PS RXZ 8S', 'Renault Pulse RxL','Renault Pulse RxZ', 'Renault Pulse RxZ Optional', 'Renault Scala Diesel RxL', 'Renault Scala RxL', 'Renault Triber RXT BSIV'))

elif brand == 'Tata':
    name = st.selectbox('Select Car Model Number',
            ('Tata Altroz XE', 'Tata Altroz XZ', 'Tata Aria Pleasure 4x2', 'Tata Aria Pure LX 4x2', 'Tata Bolt Quadrajet XE','Tata Bolt Revotron XE', 'Tata Bolt Revotron XM', 'Tata Harrier XE', 'Tata Harrier XZ BSIV', 'Tata Hexa XM', 'Tata Hexa XT', 'Tata Hexa XT 4X4', 'Tata Hexa XTA', 'Tata Indica DL', 'Tata Indica DLE', 'Tata Indica DLS', 'Tata Indica DLX', 'Tata Indica GLS BS IV', 'Tata Indica LSI', 'Tata Indica LXI', 'Tata Indica V2 2001-2011 DLS BSIII', 'Tata Indica V2 DLS BSII', 'Tata Indica Vista Aqua 1.2 Safire BSIV', 'Tata Indica Vista Aqua 1.3 Quadrajet', 'Tata Indica Vista Aqua 1.3 Quadrajet ABS BSIV', 'Tata Indica Vista Aqua 1.3 Quadrajet BSIV', 'Tata Indica Vista Aqua 1.4 TDI', 'Tata Indica Vista Aqua TDI BSIII', 'Tata Indica Vista Aura 1.2 Safire', 'Tata Indica Vista Aura 1.3 Quadrajet', 'Tata Indica Vista Aura 1.3 Quadrajet BSIV', 'Tata Indica Vista Aura Plus 1.3 Quadrajet', 'Tata Indica Vista Quadrajet 90 VX', 'Tata Indica Vista Quadrajet LS', 'Tata Indica Vista Quadrajet LX', 'Tata Indica Vista Quadrajet VX', 'Tata Indica Vista TDI LS', 'Tata Indica Vista TDI LX', 'Tata Indica Vista Terra 1.4 TDI', 'Tata Indica Vista Terra Quadrajet 1.3L', 'Tata Indica Vista Terra Quadrajet 1.3L BS IV', 'Tata Indica Vista Terra TDI BSIII', 'Tata Indigo CR4', 'Tata Indigo CS Emax CNG GLX', 'Tata Indigo CS LE (TDI) BS-III', 'Tata Indigo CS LS (TDI) BS-III', 'Tata Indigo CS LX (TDI) BS-III', 'Tata Indigo CS eLS BS IV', 'Tata Indigo CS eLX BS IV', 'Tata Indigo Classic Dicor', 'Tata Indigo GLE BSIII', 'Tata Indigo GLS', 'Tata Indigo GLX', 'Tata Indigo Grand Dicor', 'Tata Indigo Grand Petrol', 'Tata Indigo LS', 'Tata Indigo LS BSII', 'Tata Indigo LS Dicor', 'Tata Indigo LX', 'Tata Indigo LX Dicor', 'Tata Indigo TDI', 'Tata Manza Aqua Quadrajet BS IV', 'Tata Manza Aura (ABS) Quadrajet BS IV', 'Tata Manza Aura (ABS) Safire BS IV', 'Tata Manza Aura Quadrajet', 'Tata Manza Aura Quadrajet BS IV', 'Tata Manza Aura Safire', 'Tata Manza Aura Safire BS IV', 'Tata Manza Club Class Quadrajet90 EX', 'Tata Manza Club Class Quadrajet90 LS', 'Tata Manza Club Class Quadrajet90 LX', 'Tata Manza Club Class Quadrajet90 VX','Tata Manza ELAN Quadrajet BS IV', 'Tata Nano CX', 'Tata Nano CX SE', 'Tata Nano Cx BSIII', 'Tata Nano Cx BSIV', 'Tata Nano LX', 'Tata Nano LX SE', 'Tata Nano Lx', 'Tata Nano Lx BSIII', 'Tata Nano Lx BSIV', 'Tata Nano STD', 'Tata Nano Std', 'Tata Nano Std BSII', 'Tata Nano Twist XE', 'Tata Nano Twist XT', 'Tata Nano XM', 'Tata New Safari 3L Dicor LX 4x2', 'Tata New Safari 4X2', 'Tata New Safari 4X4', 'Tata New Safari 4X4 EX', 'Tata New Safari DICOR 2.2 EX 4x2', 'Tata New Safari DICOR 2.2 EX 4x4', 'Tata New Safari DICOR 2.2 GX 4x2', 'Tata New Safari DICOR 2.2 GX 4x2 BS IV', 'Tata New Safari DICOR 2.2 VX 4x2', 'Tata New Safari DICOR 2.2 VX 4x4', 'Tata New Safari Dicor EX 4X2 BS IV', 'Tata Nexon 1.2 Revotron XM', 'Tata Nexon 1.2 Revotron XZ Plus', 'Tata Nexon 1.2 Revotron XZ Plus Dual Tone', 'Tata Nexon 1.5 Revotorq XM', 'Tata Nexon 1.5 Revotorq XZ', 'Tata Safari DICOR 2.2 EX 4x2', 'Tata Safari Storme EX', 'Tata Safari Storme VX', 'Tata Safari Storme VX Varicor 400', 'Tata Spacio SA 6 Seater', 'Tata Sumo GX TC 7 Str BSIII', 'Tata Sumo GX TC 8 Str', 'Tata Sumo Gold EX', 'Tata Sumo Gold EX BSIII', 'Tata Sumo LX', 'Tata Sumo SE Plus BSIII', 'Tata Sumo Victa CX 7/9 Str BSII', 'Tata Sumo Victa EX 7/9 Str BSII', 'Tata Tiago 1.05 Revotorq XE', 'Tata Tiago 1.05 Revotorq XM', 'Tata Tiago 1.05 Revotorq XT Option','Tata Tiago 1.05 Revotorq XZ Plus', 'Tata Tiago 1.2 Revotron XE', 'Tata Tiago 1.2 Revotron XT', 'Tata Tiago 1.2 Revotron XTA', 'Tata Tiago 1.2 Revotron XZ', 'Tata Tiago 1.2 Revotron XZA', 'Tata Tiago 2019-2020 XE Diesel', 'Tata Tiago 2019-2020 XZ', 'Tata Tiago NRG Petrol', 'Tata Tiago XT', 'Tata Tiago XZA AMT', 'Tata Tigor 1.2 Revotron XM', 'Tata Tigor 1.2 Revotron XT', 'Tata Tigor 1.2 Revotron XZ Option', 'Tata Venture EX', 'Tata Winger Deluxe - Hi Roof (AC)', 'Tata Xenon XT EX 4X2', 'Tata Xenon XT EX 4X4', 'Tata Zest Quadrajet 1.3', 'Tata Zest Quadrajet 1.3 75PS XE', 'Tata Zest Quadrajet 1.3 XM', 'Tata Zest Revotron 1.2 XT', 'Tata Zest Revotron 1.2T XE', 'Tata Zest Revotron 1.2T XMS'))

elif brand == 'Toyota':
    name = st.selectbox('Select Car Model Number',
            ('Toyota Camry 2.5 Hybrid', 'Toyota Camry Hybrid 2.5', 'Toyota Camry M/t', 'Toyota Corolla AE', 'Toyota Corolla Altis 1.8 GL', 'Toyota Corolla Altis 1.8 J', 'Toyota Corolla Altis 1.8 VL AT', 'Toyota Corolla Altis 1.8 VL CVT', 'Toyota Corolla Altis D-4D J', 'Toyota Corolla Altis Diesel D4DG', 'Toyota Corolla Altis Diesel D4DGL', 'Toyota Corolla Altis Diesel D4DJ', 'Toyota Corolla Altis G', 'Toyota Corolla Altis G AT', 'Toyota Corolla Altis GL MT', 'Toyota Corolla Executive (HE)', 'Toyota Corolla H2', 'Toyota Corolla H3', 'Toyota Corolla H6', 'Toyota Etios 1.4 VXD', 'Toyota Etios 1.5 V', 'Toyota Etios Cross 1.2L G', 'Toyota Etios Cross 1.4L GD', 'Toyota Etios GD', 'Toyota Etios GD SP', 'Toyota Etios Liva 1.2 G', 'Toyota Etios Liva 1.2 V', 'Toyota Etios Liva 1.2 VX', 'Toyota Etios Liva 1.4 VD', 'Toyota Etios Liva G', 'Toyota Etios Liva GD', 'Toyota Etios Liva GD SP', 'Toyota Etios Liva VD', 'Toyota Etios Liva VX', 'Toyota Etios V', 'Toyota Etios VD', 'Toyota Etios VX', 'Toyota Etios VXD', 'Toyota Fortuner 2.7 2WD AT', 'Toyota Fortuner 2.8 2WD AT BSIV', 'Toyota Fortuner 2.8 4WD AT BSIV', 'Toyota Fortuner 3.0 Diesel', 'Toyota Fortuner 4x2 AT', 'Toyota Fortuner 4x2 Manual', 'Toyota Fortuner 4x4 MT', 'Toyota Innova 2.0 GX 8 STR BSIV', 'Toyota Innova 2.0 VX 7 Seater', 'Toyota Innova 2.5 E 8 STR', 'Toyota Innova 2.5 E Diesel MS 7-seater', 'Toyota Innova 2.5 EV Diesel MS 7 Str BSIII', 'Toyota Innova 2.5 EV Diesel PS 7 Seater BSIII', 'Toyota Innova 2.5 G (Diesel) 7 Seater', 'Toyota Innova 2.5 G (Diesel) 7 Seater BS IV', 'Toyota Innova 2.5 G (Diesel) 8 Seater', 'Toyota Innova 2.5 G (Diesel) 8 Seater BS IV', 'Toyota Innova 2.5 G1 BSIV', 'Toyota Innova 2.5 G3', 'Toyota Innova 2.5 G4 Diesel 7-seater', 'Toyota Innova 2.5 G4 Diesel 8-seater', 'Toyota Innova 2.5 GX (Diesel) 7 Seater', 'Toyota Innova 2.5 GX (Diesel) 7 Seater BS IV', 'Toyota Innova 2.5 GX (Diesel) 8 Seater', 'Toyota Innova 2.5 GX (Diesel) 8 Seater BS IV', 'Toyota Innova 2.5 GX 7 STR', 'Toyota Innova 2.5 GX 7 STR BSIV', 'Toyota Innova 2.5 GX 8 STR BSIV', 'Toyota Innova 2.5 V Diesel 7-seater', 'Toyota Innova 2.5 V Diesel 8-seater', 'Toyota Innova 2.5 VX (Diesel) 7 Seater', 'Toyota Innova 2.5 VX (Diesel) 7 Seater BS IV', 'Toyota Innova 2.5 VX (Diesel) 8 Seater', 'Toyota Innova 2.5 VX (Diesel) 8 Seater BS IV', 'Toyota Innova 2.5 VX 8 STR', 'Toyota Innova 2.5 VX 8 STR BSIV', 'Toyota Innova 2.5 Z Diesel 7 Seater BS IV', 'Toyota Innova Crysta 2.4 G MT BSIV', 'Toyota Innova Crysta 2.4 GX AT', 'Toyota Innova Crysta 2.4 GX MT 8S BSIV', 'Toyota Innova Crysta 2.4 VX MT', 'Toyota Innova Crysta 2.4 VX MT 8S BSIV', 'Toyota Innova Crysta 2.4 VX MT BSIV', 'Toyota Innova Crysta 2.4 ZX MT', 'Toyota Innova Crysta 2.5 VX BS IV', 'Toyota Innova Crysta 2.8 GX AT BSIV', 'Toyota Innova Crysta 2.8 ZX AT BSIV', 'Toyota Qualis FS B3', 'Toyota Yaris G'))

elif brand == 'Volkswagen':
    name = st.selectbox('Select Car Model Number',
            ('Volkswagen Ameo 1.2 MPI Trendline', 'Volkswagen Ameo 1.5 TDI Comfortline', 'Volkswagen Ameo 1.5 TDI Highline','Volkswagen Ameo 1.5 TDI Highline 16 Alloy', 'Volkswagen Ameo 1.5 TDI Highline Plus 16', 'Volkswagen CrossPolo 1.2 MPI', 'Volkswagen Jetta 1.4 TSI Comfortline', 'Volkswagen Jetta 1.9 Highline TDI', 'Volkswagen Jetta 1.9 L TDI', 'Volkswagen Jetta 1.9 TDI Comfortline DSG', 'Volkswagen Jetta 1.9 TDI Trendline', 'Volkswagen Jetta 2.0 TDI Comfortline', 'Volkswagen Jetta 2.0 TDI Trendline', 'Volkswagen Jetta 2.0L TDI Comfortline', 'Volkswagen Jetta 2.0L TDI Highline', 'Volkswagen Jetta 2.0L TDI Highline AT', 'Volkswagen Passat 1.8 TSI MT', 'Volkswagen Polo 1.0 MPI Trendline', 'Volkswagen Polo 1.0 TSI Highline Plus', 'Volkswagen Polo 1.2 MPI Comfortline', 'Volkswagen Polo 1.2 MPI Highline', 'Volkswagen Polo 1.5 TDI Comfortline','Volkswagen Polo 1.5 TDI Highline', 'Volkswagen Polo 1.5 TDI Trendline', 'Volkswagen Polo 2015-2019 1.2 MPI Highline', 'Volkswagen Polo Diesel Comfortline 1.2L', 'Volkswagen Polo Diesel Highline 1.2L', 'Volkswagen Polo Diesel Trendline 1.2L', 'Volkswagen Polo GT 1.0 TSI', 'Volkswagen Polo GTI', 'Volkswagen Polo Petrol Comfortline 1.2L', 'Volkswagen Polo Petrol Highline 1.2L', 'Volkswagen Polo SR Petrol 1.2L', 'Volkswagen Vento 1.0 TSI Highline Plus', 'Volkswagen Vento 1.5 Highline Plus AT 16 Alloy', 'Volkswagen Vento 1.5 TDI Comfortline', 'Volkswagen Vento 1.5 TDI Comfortline AT', 'Volkswagen Vento 1.5 TDI Highline', 'Volkswagen Vento 1.5 TDI Highline AT', 'Volkswagen Vento 1.5 TDI Highline BSIV', 'Volkswagen Vento 1.5 TDI Highline Plus AT', 'Volkswagen Vento 1.5 TDI Highline Plus AT BSIV', 'Volkswagen Vento 1.6 Highline', 'Volkswagen Vento Celeste 1.5 TDI Highline AT', 'Volkswagen Vento Diesel Comfortline', 'Volkswagen Vento Diesel Highline', 'Volkswagen Vento Diesel Style Limited Edition','Volkswagen Vento Diesel Trendline', 'Volkswagen Vento IPL II Diesel Trendline', 'Volkswagen Vento Magnific 1.6 Highline', 'Volkswagen Vento New Diesel Highline', 'Volkswagen Vento Petrol Highline', 'Volkswagen Vento Petrol Highline AT'))


# year
year = st.slider('Year', 1992, 2020)


# fuel
fuel = st.selectbox('Select the Fuel Type',
        ('CNG', 'Diesel', 'LPG', 'Petrol'))


# seller_type
seller_type = st.selectbox('Select the type of Seller',
                ('Individual', 'Dealer', 'Trustmark Dealer'))


# transmission
transmission = st.selectbox('Select the transmission',
                ('Manual', 'Automatic'))


# owner
owner = st.selectbox('Select the type of Owner',
    ('First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'))


# km_driven
km_driven = st.slider('KM Driven', 1, 806599)
number = st.number_input(value=None, placeholder="Kilometer driven by your car...")

# Predict Button

if st.button('Predict'):
    st.write('Predicted Value: ')

    if brand == 'Ambassador':
        brand_enc = 0
        name_enc = 976
    elif brand == 'Audi': 
        brand_enc = 1
        name_enc = 976
    elif brand == 'BMW': 
        brand_enc = 2
        name_enc = 976
    elif brand == 'Daewoo':
        brand_enc = 4
        name_enc = 976
    elif brand == 'Datsun':
        brand_enc = 5
        name_enc = 976
    elif brand == 'Fiat':
        brand_enc = 6
        name_enc = 976
    elif brand == 'Jaguar': 
        brand_enc = 12
        name_enc = 976
    elif brand == 'Jeep':
        brand_enc = 13
        name_enc = 976
    elif brand == 'Kia':
        brand_enc = 14
        name_enc = 976
    elif brand == 'Land': 
        brand_enc = 15
        name_enc = 976
    elif brand == 'MG':
        brand_enc = 16
        name_enc = 976
    elif brand == 'Mercedes-Benz':
        brand_enc = 19
        name_enc = 976
    elif brand == 'Mitsubish':
        brand_enc = 20
        name_enc = 976
    elif brand == 'Nissan':
        brand_enc = 21
        name_enc = 976
    elif brand == 'OpelCorsa':
        brand_enc = 22
        name_enc = 976
    elif brand == 'Skoda':
        brand_enc = 24
        name_enc = 976
    elif brand == 'Volvo':
        brand_enc = 28
        name_enc = 976

    elif brand == 'Chevrolet':
        brand_enc = 3
        if name == 'Chevrolet Aveo 1.4':
            name_enc = 0
        elif name == 'Chevrolet Aveo 1.4 CNG':
            name_enc = 1
        elif name == 'Chevrolet Aveo 1.4 LS':
            name_enc = 2
        elif name == 'Chevrolet Aveo 1.4 LT BSIV':
            name_enc = 3
        elif name == 'Chevrolet Aveo 1.6 LT':
            name_enc = 4
        elif name == 'Chevrolet Aveo 1.6 LT with ABS':
            name_enc = 5
        elif name == 'Chevrolet Aveo U-VA 1.2':
            name_enc = 6
        elif name == 'Chevrolet Aveo U-VA 1.2 LS':
            name_enc = 7
        elif name == 'Chevrolet Aveo U-VA 1.2 LT':
            name_enc = 8
        elif name == 'Chevrolet Aveo U-VA 1.2 LT WO ABS Airbag':
            name_enc = 9
        elif name == 'Chevrolet Beat Diesel':
            name_enc = 10
        elif name == 'Chevrolet Beat Diesel LS':
            name_enc = 11
        elif name == 'Chevrolet Beat Diesel LT':
            name_enc = 12
        elif name == 'Chevrolet Beat Diesel LT Option':
            name_enc = 13
        elif name == 'Chevrolet Beat Diesel PS':
            name_enc = 14
        elif name == 'Chevrolet Beat LS':
            name_enc = 15
        elif name == 'Chevrolet Beat LT':
            name_enc = 16
        elif name == 'Chevrolet Beat LT LPG':
            name_enc = 17
        elif name == 'Chevrolet Beat LT Option':
            name_enc = 18
        elif name == 'Chevrolet Beat PS':
            name_enc = 19
        elif name == 'Chevrolet Captiva 2.0L VCDi':
            name_enc = 20
        elif name == 'Chevrolet Captiva LT':
            name_enc = 21
        elif name == 'Chevrolet Cruze LT':
            name_enc = 22
        elif name == 'Chevrolet Cruze LTZ':
            name_enc = 23
        elif name == 'Chevrolet Cruze LTZ AT':
            name_enc = 24
        elif name == 'Chevrolet Enjoy 1.3 TCDi LS 8':
            name_enc = 25
        elif name == 'Chevrolet Enjoy TCDi LS 8 Seater':
            name_enc = 26
        elif name == 'Chevrolet Enjoy TCDi LT 7 Seater':
            name_enc = 27
        elif name == 'Chevrolet Enjoy TCDi LT 8 Seater':
            name_enc = 28
        elif name == 'Chevrolet Enjoy TCDi LTZ 7 Seater':
            name_enc = 29
        elif name == 'Chevrolet Optra 1.6':
            name_enc = 30
        elif name == 'Chevrolet Optra 1.6 LS':
            name_enc = 31
        elif name == 'Chevrolet Optra Magnum 2.0 LS':
            name_enc = 32
        elif name == 'Chevrolet Optra Magnum 2.0 LS BSIII':
            name_enc = 33
        elif name == 'Chevrolet Optra Magnum 2.0 LT':
            name_enc = 34
        elif name == 'Chevrolet Sail 1.2 Base':
            name_enc = 35
        elif name == 'Chevrolet Sail 1.2 LT ABS':
            name_enc = 36
        elif name == 'Chevrolet Sail 1.3 LS':
            name_enc = 37
        elif name == 'Chevrolet Sail Hatchback 1.2 LS':
            name_enc = 38
        elif name == 'Chevrolet Sail Hatchback 1.3 TCDi':
            name_enc = 39
        elif name == 'Chevrolet Sail Hatchback 1.3 TCDi LT ABS':
            name_enc = 40
        elif name == 'Chevrolet Sail Hatchback LS ABS':
            name_enc = 41
        elif name == 'Chevrolet Sail Hatchback LT ABS':
            name_enc = 42
        elif name == 'Chevrolet Sail LS ABS':
            name_enc = 43
        elif name == 'Chevrolet Spark 1.0':
            name_enc = 44
        elif name == 'Chevrolet Spark 1.0 LS':
            name_enc = 45
        elif name == 'Chevrolet Spark 1.0 LT':
            name_enc = 46
        elif name == 'Chevrolet Spark 1.0 LT BS3':
            name_enc = 47
        elif name == 'Chevrolet Spark 1.0 LT Option Pack w/ Airbag':
            name_enc = 48
        elif name == 'Chevrolet Spark 1.0 PS':
            name_enc = 49
        elif name == 'Chevrolet Tavera LS B3 7 Seats BSII':
            name_enc = 50
        elif name == 'Chevrolet Tavera LT L1 7 Seats BSIII':
            name_enc = 51
        elif name == 'Chevrolet Tavera Neo 2 LS B4 7 Str BSIII':
            name_enc = 52
        elif name == 'Chevrolet Tavera Neo 2 LT L 9 Str':
            name_enc = 53
        elif name == 'Chevrolet Tavera Neo 3 10 Seats BSIV':
            name_enc = 54
        elif name == 'Chevrolet Tavera Neo 3 9 Str BSIII': 
            name_enc = 55
        elif name == 'Chevrolet Tavera Neo 3 LS 7 C BSIII':
            name_enc = 56
        elif name == 'Chevrolet Tavera Neo 3 LT 9 Seats BSIII':
            name_enc = 57
        elif name == 'Chevrolet Tavera Neo 3 Max 9 Str BSIII':
            name_enc = 58
        elif name == 'Chevrolet Tavera Neo LS B3 - 7(C) seats BSIII':
            name_enc = 59

    elif brand == 'Ford':
        brand_enc = 8
        if name == 'Ford Aspire Titanium BSIV':
            name_enc = 60 
        elif name == 'Ford Aspire Titanium Diesel BSIV':
            name_enc = 61
        elif name == 'Ford Aspire Titanium Plus BSIV':
            name_enc = 62
        elif name == 'Ford Aspire Titanium Plus Diesel BSIV':
            name_enc = 63
        elif name == 'Ford Classic 1.4 Duratorq LXI':
            name_enc = 64
        elif name == 'Ford Classic 1.6 Duratec LXI':
            name_enc = 65
        elif name == 'Ford EcoSport 1.5 Diesel Ambiente BSIV':
            name_enc = 66
        elif name == 'Ford EcoSport 1.5 Diesel Titanium BSIV':
            name_enc = 67
        elif name == 'Ford EcoSport 1.5 Diesel Titanium Plus BSIV':
            name_enc = 68
        elif name == 'Ford EcoSport 1.5 Diesel Trend BSIV':
            name_enc = 69
        elif name == 'Ford EcoSport 1.5 Diesel Trend Plus BSIV':
            name_enc = 70
        elif name == 'Ford EcoSport 1.5 Petrol Titanium BSIV':
            name_enc = 71
        elif name == 'Ford EcoSport 1.5 Petrol Titanium Plus AT BSIV':
            name_enc = 72
        elif name == 'Ford EcoSport 1.5 TDCi Titanium BSIV':
            name_enc = 73
        elif name == 'Ford EcoSport 1.5 TDCi Titanium Plus BE BSIV':
            name_enc = 74
        elif name == 'Ford EcoSport 1.5 TDCi Titanium Plus BSIV':
            name_enc = 75
        elif name == 'Ford EcoSport 1.5 Ti VCT MT Titanium BE BSIV':
            name_enc = 76
        elif name == 'Ford EcoSport 1.5 Ti VCT MT Titanium BSIV':
            name_enc = 77
        elif name == 'Ford EcoSport 1.5 Ti VCT MT Trend BSIV':
            name_enc = 78
        elif name == 'Ford Ecosport 1.0 Ecoboost Platinum Edition BSIV':
            name_enc = 79
        elif name == 'Ford Ecosport 1.0 Ecoboost Titanium':
            name_enc = 80
        elif name == 'Ford Ecosport 1.0 Ecoboost Titanium Optional':
            name_enc = 81
        elif name == 'Ford Ecosport 1.5 DV5 MT Ambiente':
            name_enc = 82
        elif name == 'Ford Ecosport 1.5 DV5 MT Titanium':
            name_enc = 83
        elif name == 'Ford Ecosport 1.5 DV5 MT Titanium Optional':
            name_enc = 84
        elif name == 'Ford Ecosport 1.5 DV5 MT Trend':
            name_enc = 85
        elif name == 'Ford Ecosport 1.5 Diesel Titanium':
            name_enc = 86
        elif name == 'Ford Ecosport 1.5 Diesel Titanium Plus':
            name_enc = 87
        elif name == 'Ford Ecosport 1.5 Petrol Ambiente':
            name_enc = 88
        elif name == 'Ford Ecosport 1.5 Petrol Titanium Plus':
            name_enc = 89
        elif name == 'Ford Ecosport 1.5 Petrol Titanium Plus AT':
            name_enc = 90
        elif name == 'Ford Ecosport 1.5 Petrol Trend':
            name_enc = 91
        elif name == 'Ford Ecosport 1.5 Ti VCT AT Titanium':
            name_enc = 92
        elif name == 'Ford Ecosport Sports Petrol':
            name_enc = 93
        elif name == 'Ford Ecosport Thunder Edition Diesel':
            name_enc = 94
        elif name == 'Ford Endeavour 2.2 Titanium AT 4X2':
            name_enc = 95
        elif name == 'Ford Endeavour 2.5L 4X2':
            name_enc = 96
        elif name == 'Ford Endeavour 2.5L 4X2 MT':
            name_enc = 97
        elif name == 'Ford Endeavour 3.0L 4X4 AT':
            name_enc = 98
        elif name == 'Ford Endeavour 3.2 Titanium AT 4X4':
            name_enc = 99
        elif name == 'Ford Endeavour 4x2 XLT':
            name_enc = 100
        elif name == 'Ford Endeavour 4x4 XLT':
            name_enc = 101
        elif name == 'Ford Endeavour Hurricane Limited Edition':
            name_enc = 102
        elif name == 'Ford Endeavour Titanium 4X2':
            name_enc = 103
        elif name == 'Ford Endeavour Titanium Plus 4X4':
            name_enc = 104
        elif name == 'Ford Endeavour XLT TDCi 4X2':
            name_enc = 105
        elif name == 'Ford Fiesta 1.4 Duratec ZXI':
            name_enc = 106
        elif name == 'Ford Fiesta 1.4 SXi TDCi':
            name_enc = 107
        elif name == 'Ford Fiesta 1.4 SXi TDCi ABS':
            name_enc = 108
        elif name == 'Ford Fiesta 1.4 ZXi Duratec':
            name_enc = 109
        elif name == 'Ford Fiesta 1.4 ZXi Leather':
            name_enc = 110
        elif name == 'Ford Fiesta 1.4 ZXi TDCi ABS':
            name_enc = 111
        elif name == 'Ford Fiesta 1.5 TDCi Ambiente':
            name_enc = 112
        elif name == 'Ford Fiesta 1.5 TDCi Titanium':
            name_enc = 113
        elif name == 'Ford Fiesta 1.6 Duratec EXI Ltd':
            name_enc = 114
        elif name == 'Ford Fiesta 1.6 Duratec S':
            name_enc = 115
        elif name == 'Ford Fiesta 1.6 ZXi Duratec':
            name_enc = 116
        elif name == 'Ford Fiesta 1.6 ZXi Leather':
            name_enc = 117
        elif name == 'Ford Fiesta Classic 1.4 Duratorq CLXI':
            name_enc = 118
        elif name == 'Ford Fiesta Classic 1.4 SXI Duratorq':
            name_enc = 119
        elif name == 'Ford Fiesta Classic 1.6 Duratec CLXI':
            name_enc = 120
        elif name == 'Ford Fiesta Diesel Style':
            name_enc = 121
        elif name == 'Ford Fiesta Diesel Trend':
            name_enc = 122
        elif name == 'Ford Fiesta Petrol Trend':
            name_enc = 123
        elif name == 'Ford Fiesta Titanium 1.5 TDCi':
            name_enc = 124
        elif name == 'Ford Figo 1.2P Ambiente MT':
            name_enc = 125
        elif name == 'Ford Figo 1.2P Titanium MT':
            name_enc = 126
        elif name == 'Ford Figo 1.2P Titanium Plus MT':
            name_enc = 127
        elif name == 'Ford Figo 1.5 Sports Edition MT':
            name_enc = 128
        elif name == 'Ford Figo 1.5D Ambiente ABS MT':
            name_enc = 129
        elif name == 'Ford Figo 1.5D Titanium MT':
            name_enc = 130
        elif name == 'Ford Figo 1.5D Titanium Opt MT':
            name_enc = 131
        elif name == 'Ford Figo 1.5D Trend MT':
            name_enc = 132
        elif name == 'Ford Figo 1.5P Titanium AT':
            name_enc = 133
        elif name == 'Ford Figo Aspire 1.2 Ti-VCT Titanium Plus':
            name_enc = 134
        elif name == 'Ford Figo Aspire 1.2 Ti-VCT Trend':
            name_enc = 135
        elif name == 'Ford Figo Aspire 1.5 TDCi Ambiente ABS':
            name_enc = 136
        elif name == 'Ford Figo Aspire 1.5 TDCi Titanium':
            name_enc = 137
        elif name == 'Ford Figo Aspire 1.5 TDCi Titanium Plus':
            name_enc = 138
        elif name == 'Ford Figo Aspire 1.5 TDCi Trend':
            name_enc = 139
        elif name == 'Ford Figo Aspire 1.5 Ti-VCT Titanium':
            name_enc = 140
        elif name == 'Ford Figo Aspire Facelift':
            name_enc = 141
        elif name == 'Ford Figo Aspire Titanium Plus Diesel':
            name_enc = 142
        elif name == 'Ford Figo Diesel Celebration Edition':
            name_enc = 143
        elif name == 'Ford Figo Diesel EXI':
            name_enc = 144
        elif name == 'Ford Figo Diesel LXI':
            name_enc = 145
        elif name == 'Ford Figo Diesel Titanium':
            name_enc = 146
        elif name == 'Ford Figo Diesel ZXI':
            name_enc = 147
        elif name == 'Ford Figo Petrol EXI':
            name_enc = 148
        elif name == 'Ford Figo Petrol LXI':
            name_enc = 149
        elif name == 'Ford Figo Petrol Titanium':
            name_enc = 150
        elif name == 'Ford Figo Petrol ZXI':
            name_enc = 151
        elif name == 'Ford Figo Titanium':
            name_enc = 152
        elif name == 'Ford Figo Titanium Diesel BSIV':
            name_enc = 153
        elif name == 'Ford Figo Trend':
            name_enc = 154
        elif name == 'Ford Freestyle Titanium':
            name_enc = 155
        elif name == 'Ford Freestyle Titanium Diesel':
            name_enc = 156
        elif name == 'Ford Freestyle Titanium Diesel BSIV':
            name_enc = 157
        elif name == 'Ford Freestyle Titanium Plus':
            name_enc = 158
        elif name == 'Ford Freestyle Titanium Plus Diesel':
            name_enc = 159
        elif name == 'Ford Freestyle Titanium Plus Diesel BSIV':
            name_enc = 160
        elif name == 'Ford Freestyle Trend Petrol BSIV':
            name_enc = 161
        elif name == 'Ford Fusion 1.6 Duratec Petrol':
            name_enc = 162
        elif name == 'Ford Ikon 1.3 Flair':
            name_enc = 163
        elif name == 'Ford Ikon 1.3L Rocam Flair':
            name_enc = 164
        elif name == 'Ford Ikon 1.4 TDCi DuraTorq':
            name_enc = 165
        elif name == 'Ford Ikon 1.4 ZXi':
            name_enc = 166
        elif name == 'Ford Ikon 1.6 ZXI NXt':
            name_enc = 167
        elif name == 'Ford Ikon 1.8 D':
            name_enc = 168
        
    elif brand == 'Honda':
        brand_enc = 9
        if name == 'Honda Accord 2.4 AT':
            name_enc = 169
        elif name == 'Honda Accord 2.4 MT':
            name_enc = 170
        elif name == 'Honda Accord VTi-L (MT)':
            name_enc = 171
        elif name == 'Honda Amaze E i-DTEC':
            name_enc = 172
        elif name == 'Honda Amaze E i-Dtech':
            name_enc = 173
        elif name == 'Honda Amaze E i-VTEC':
            name_enc = 174
        elif name == 'Honda Amaze E i-Vtech':
            name_enc = 175
        elif name == 'Honda Amaze EX i-Dtech':
            name_enc = 176
        elif name == 'Honda Amaze S AT i-Vtech':
            name_enc = 177
        elif name == 'Honda Amaze S CVT Petrol':
            name_enc = 178
        elif name == 'Honda Amaze S Diesel':
            name_enc = 179
        elif name == 'Honda Amaze S Petrol BSIV':
            name_enc = 180
        elif name == 'Honda Amaze S i-DTEC':
            name_enc = 181
        elif name == 'Honda Amaze S i-Dtech':
            name_enc = 182
        elif name == 'Honda Amaze S i-VTEC':
            name_enc = 183
        elif name == 'Honda Amaze S i-Vtech':
            name_enc = 184
        elif name == 'Honda Amaze SX i-VTEC':
            name_enc = 185
        elif name == 'Honda Amaze V CVT Petrol BSIV':
            name_enc = 186
        elif name == 'Honda Amaze V Diesel BSIV':
            name_enc = 187
        elif name == 'Honda Amaze VX AT i-Vtech':
            name_enc = 188
        elif name == 'Honda Amaze VX Diesel BSIV':
            name_enc = 189
        elif name == 'Honda Amaze VX O iDTEC':
            name_enc = 190
        elif name == 'Honda Amaze VX Petrol BSIV':
            name_enc = 191
        elif name == 'Honda Amaze VX i-DTEC':
            name_enc = 192
        elif name == 'Honda Amaze VX i-VTEC':
            name_enc = 193
        elif name == 'Honda BR-V i-DTEC VX MT':
            name_enc = 194
        elif name == 'Honda BR-V i-VTEC S MT':
            name_enc = 195
        elif name == 'Honda BR-V i-VTEC VX MT':
            name_enc = 196
        elif name == 'Honda BRV i-DTEC V MT':
            name_enc = 197
        elif name == 'Honda BRV i-VTEC V MT':
            name_enc = 198
        elif name == 'Honda Brio 1.2 E MT':
            name_enc = 199
        elif name == 'Honda Brio 1.2 S MT':
            name_enc = 200
        elif name == 'Honda Brio 1.2 S Option MT':
            name_enc = 201
        elif name == 'Honda Brio 1.2 VX MT':
            name_enc = 202
        elif name == 'Honda Brio E MT':
            name_enc = 203
        elif name == 'Honda Brio Exclusive Edition':
            name_enc = 204
        elif name == 'Honda Brio S MT':
            name_enc = 205
        elif name == 'Honda Brio S Option AT':
            name_enc = 206
        elif name == 'Honda Brio V MT':
            name_enc = 207
        elif name == 'Honda Brio VX':
            name_enc = 208
        elif name == 'Honda CR-V Diesel 4WD':
            name_enc = 209
        elif name == 'Honda City 1.3 DX':
            name_enc = 210
        elif name == 'Honda City 1.3 EXI':
            name_enc = 211
        elif name == 'Honda City 1.5 E MT':
            name_enc = 212
        elif name == 'Honda City 1.5 EXI':
            name_enc = 213
        elif name == 'Honda City 1.5 EXI S':
            name_enc = 214
        elif name == 'Honda City 1.5 GXI':
            name_enc = 215
        elif name == 'Honda City 1.5 S MT':
            name_enc = 216
        elif name == 'Honda City 1.5 V AT':
            name_enc = 217
        elif name == 'Honda City 1.5 V AT Exclusive':
            name_enc = 218
        elif name == 'Honda City 1.5 V Elegance':
            name_enc = 219
        elif name == 'Honda City 1.5 V MT':
            name_enc = 220
        elif name == 'Honda City Corporate Edition':
            name_enc = 221
        elif name == 'Honda City E':
            name_enc = 222
        elif name == 'Honda City Edge Edition Diesel SV':
            name_enc = 223
        elif name == 'Honda City S':
            name_enc = 224
        elif name == 'Honda City V AT':
            name_enc = 225
        elif name == 'Honda City V MT':
            name_enc = 226
        elif name == 'Honda City VTEC':
            name_enc = 227
        elif name == 'Honda City VX CVT':
            name_enc = 228
        elif name == 'Honda City VX MT':
            name_enc = 229
        elif name == 'Honda City i DTEC E':
            name_enc = 230
        elif name == 'Honda City i DTEC S':
            name_enc = 231
        elif name == 'Honda City i DTEC SV':
            name_enc = 232
        elif name == 'Honda City i DTEC V':
            name_enc = 233
        elif name == 'Hona City i DTEC VX':
            name_enc = 234
        elif name == 'Honda City i DTec SV':
            name_enc = 235
        elif name == 'Honda City i DTec V':
            name_enc = 236
        elif name == 'Honda City i VTEC S':
            name_enc = 237
        elif name == 'Honda City i VTEC SV':
            name_enc = 238
        elif name == 'Honda City i VTEC V':
            name_enc = 239
        elif name == 'Honda City i VTEC VX':
            name_enc = 240
        elif name == 'Honda City i-DTEC SV':
            name_enc = 241
        elif name == 'Honda City i-DTEC V':
            name_enc = 242
        elif name == 'Honda City i-DTEC VX':
            name_enc = 243
        elif name == 'Honda City i-DTEC ZX':
            name_enc = 244
        elif name == 'Honda City i-VTEC CVT VX':
            name_enc = 245
        elif name == 'Honda City i-VTEC CVT ZX':
            name_enc = 246
        elif name == 'Honda City i-VTEC SV':
            name_enc = 247
        elif name == 'Honda City i-VTEC VX':
            name_enc = 248
        elif name == 'Honda City i-VTEC ZX':
            name_enc = 249
        elif name == 'Honda Civic 1.8 (E) MT':
            name_enc = 250
        elif name == 'Honda Civic 1.8 MT Sport':
            name_enc = 251
        elif name == 'Honda Civic 1.8 S AT':
            name_enc = 252
        elif name == 'Honda Civic 1.8 S MT':
            name_enc = 253
        elif name == 'Honda Civic 1.8 V AT':
            name_enc = 254
        elif name == 'Honda Civic 1.8 V MT':
            name_enc = 255
        elif name == 'Honda Jazz 1.2 S i VTEC':
            name_enc = 256
        elif name == 'Honda Jazz 1.2 V i VTEC':
            name_enc = 257
        elif name == 'Honda Jazz 1.2 VX i VTEC':
            name_enc = 258
        elif name == 'Honda Jazz 1.5 E i DTEC':
            name_enc = 259
        elif name == 'Honda Jazz 1.5 S i DTEC':
            name_enc = 260
        elif name == 'Honda Jazz 1.5 SV i DTEC':
            name_enc = 261
        elif name == 'Honda Jazz 1.5 V i DTEC':
            name_enc = 262
        elif name == 'Honda Jazz 1.5 VX i DTEC':
            name_enc = 263
        elif name == 'Honda Jazz S':
            name_enc = 264
        elif name == 'Honda Jazz Select Edition':
            name_enc = 265
        elif name == 'Honda Jazz Select Edition Active':
            name_enc = 266
        elif name == 'Honda Jazz V':
            name_enc = 267
        elif name == 'Honda Jazz VX':
            name_enc = 268
        elif name == 'Honda Jazz VX CVT':
            name_enc = 269
        elif name == 'Honda Mobilio E i DTEC':
            name_enc = 270
        elif name == 'Honda Mobilio S i DTEC':
            name_enc = 271
        elif name == 'Honda Mobilio S i VTEC':
            name_enc = 272
        elif name == 'Honda Mobilio V i DTEC':
            name_enc = 273
        elif name == 'Honda Mobilio V i VTEC':
            name_enc = 274
        elif name == 'Honda WR-V i-DTEC V':
            name_enc = 275
        elif name == 'Honda WR-V i-DTEC VX':
            name_enc = 276
        elif name == 'Honda WR-V i-VTEC VX':
            name_enc = 277

    elif brand == 'Hyundai':
        brand_enc = 10
        if name == 'Hyundai Accent CRDi':
            name_enc = 278
        elif name == 'Hyundai Accent Executive':
            name_enc = 279
        elif name == 'Hyundai Accent Executive CNG':
            name_enc = 280
        elif name == 'Hyundai Accent GLE':
            name_enc = 281
        elif name == 'Hyundai Accent GLE 1':
            name_enc = 282
        elif name == 'Hyundai Accent GLE CNG':
            name_enc = 283
        elif name == 'Hyundai Accent GLS':
            name_enc = 284
        elif name == 'Hyundai Accent GLS 1.6 ABS':
            name_enc = 285
        elif name == 'Hyundai Accent GLX':
            name_enc = 286
        elif name == 'Hyundai Creta 1.4 CRDi Base':
            name_enc = 287
        elif name == 'Hyundai Creta 1.4 CRDi S':
            name_enc = 288
        elif name == 'Hyundai Creta 1.4 CRDi S Plus':
            name_enc = 289
        elif name == 'Hyundai Creta 1.4 E Plus':
            name_enc = 290
        elif name == 'Hyundai Creta 1.4 EX Diesel':
            name_enc = 291
        elif name == 'Hyundai Creta 1.6 CRDi AT SX Plus':
            name_enc = 292
        elif name == 'Hyundai Creta 1.6 CRDi SX':
            name_enc = 293
        elif name == 'Hyundai Creta 1.6 CRDi SX Option':
            name_enc = 294
        elif name == 'Hyundai Creta 1.6 CRDi SX Plus':
            name_enc = 295
        elif name == 'Hyundai Creta 1.6 E Plus':
            name_enc = 296
        elif name == 'Hyundai Creta 1.6 Gamma SX Plus':
            name_enc = 297
        elif name == 'Hyundai Creta 1.6 SX':
            name_enc = 298
        elif name == 'Hyundai Creta 1.6 SX Automatic':
            name_enc = 299
        elif name == 'Hyundai Creta 1.6 SX Automatic Diesel':
            name_enc = 300
        elif name == 'Hyundai Creta 1.6 SX Option':
            name_enc = 301
        elif name == 'Hyundai Creta 1.6 VTVT AT SX Plus':
            name_enc = 302
        elif name == 'Hyundai Creta 1.6 VTVT S':
            name_enc = 303
        elif name == 'Hyundai EON 1.0 Era Plus':
            name_enc = 304
        elif name == 'Hyundai EON 1.0 Kappa Magna Plus':
            name_enc = 305
        elif name == 'Hyundai EON D Lite':
            name_enc = 306
        elif name == 'Hyundai EON D Lite Plus':
            name_enc = 307
        elif name == 'Hyundai EON Era':
            name_enc = 307
        elif name == 'Hyundai EON Era Plus':
            name_enc = 309
        elif name == 'Hyundai EON Era Plus Option':
            name_enc = 310
        elif name == 'Hyundai EON Era Plus Sports Edition':
            name_enc = 311
        elif name == 'Hyundai EON LPG Magna Plus':
            name_enc = 312
        elif name == 'Hyundai EON Magna':
            name_enc = 313
        elif name == 'Hyundai EON Magna Optional':
            name_enc = 314
        elif name == 'Hyundai EON Magna Plus':
            name_enc = 315
        elif name == 'Hyundai EON Magna Plus Option':
            name_enc = 316
        elif name == 'Hyundai EON Sportz':
            name_enc = 317
        elif name == 'Hyundai Elantra 2.0 SX AT':
            name_enc = 318
        elif name == 'Hyundai Elantra CRDi (Leather Option)':
            name_enc = 319
        elif name == 'Hyundai Elantra CRDi S':
            name_enc = 320
        elif name == 'Hyundai Elantra CRDi SX':
            name_enc = 321
        elif name == 'Hyundai Elantra SX':
            name_enc = 322
        elif name == 'Hyundai Elite i20 Asta Option BSIV':
            name_enc = 323
        elif name == 'Hyundai Elite i20 Asta Option CVT BSIV':
            name_enc = 324
        elif name == 'Hyundai Elite i20 Diesel Asta Option':
            name_enc = 325
        elif name == 'Hyundai Elite i20 Diesel Era':
            name_enc = 326
        elif name == 'Hyundai Elite i20 Magna Plus BSIV':
            name_enc = 327
        elif name == 'Hyundai Elite i20 Magna Plus Diesel':
            name_enc = 328
        elif name == 'Hyundai Elite i20 Petrol Asta Option':
            name_enc = 329
        elif name == 'Hyundai Elite i20 Petrol Magna Exective':
            name_enc = 330
        elif name == 'Hyundai Elite i20 Sportz Plus BSIV':
            name_enc = 331
        elif name == 'Hyundai Elite i20 Sportz Plus CVT BSIV':
            name_enc = 332
        elif name == 'Hyundai Elite i20 Sportz Plus Dual Tone BSIV':
            name_enc = 333
        elif name == 'Hyundai Getz 1.3 GLS':
            name_enc = 334
        elif name == 'Hyundai Getz 1.3 GVS':
            name_enc = 335
        elif name == 'Hyundai Getz 1.5 CRDi GVS':
            name_enc = 336
        elif name == 'Hyundai Getz GL':
            name_enc = 337
        elif name == 'Hyundai Getz GLE':
            name_enc = 338
        elif name == 'Hyundai Getz GLS':
            name_enc = 339
        elif name == 'Hyundai Getz GLS ABS':
            name_enc = 340
        elif name == 'Hyundai Getz GLX':
            name_enc = 341
        elif name == 'Hyundai Grand i10 1.2 CRDi Asta':
            name_enc = 342
        elif name == 'Hyundai Grand i10 1.2 CRDi Magna':
            name_enc = 343
        elif name == 'Hyundai Grand i10 1.2 CRDi Sportz Option':
            name_enc = 344
        elif name == 'Hyundai Grand i10 1.2 Kappa Asta':
            name_enc = 345
        elif name == 'Hyundai Grand i10 1.2 Kappa Era':
            name_enc = 346
        elif name == 'Hyundai Grand i10 1.2 Kappa Magna AT':
            name_enc = 347
        elif name == 'Hyundai Grand i10 1.2 Kappa Magna BSIV':
            name_enc = 348
        elif name == 'Hyundai Grand i10 1.2 Kappa Sportz AT':
            name_enc = 349
        elif name == 'Hyundai Grand i10 1.2 Kappa Sportz BSIV':
            name_enc = 350
        elif name == 'Hyundai Grand i10 1.2 Kappa Sportz Dual Tone':
            name_enc = 351
        elif name == 'Hyundai Grand i10 1.2 Kappa Sportz Option':
            name_enc = 352
        elif name == 'Hyundai Grand i10 AT Asta':
            name_enc = 353
        elif name == 'Hyundai Grand i10 Asta':
            name_enc = 354
        elif name == 'Hyundai Grand i10 Asta Option':
            name_enc = 355
        elif name == 'Hyundai Grand i10 Asta Option AT':
            name_enc = 356
        elif name == 'Hyundai Grand i10 CRDi Asta':
            name_enc = 357
        elif name == 'Hyundai Grand i10 CRDi Asta Option':
            name_enc = 358
        elif name == 'Hyundai Grand i10 CRDi Magna':
            name_enc = 359
        elif name == 'Hyundai Grand i10 CRDi Sportz':
            name_enc = 360
        elif name == 'Hyundai Grand i10 Magna':
            name_enc = 361
        elif name == 'Hyundai Grand i10 Magna AT':
            name_enc = 362
        elif name == 'Hyundai Grand i10 Nios AMT Magna':
            name_enc = 363
        elif name == 'Hyundai Grand i10 Nios Magna CRDi':
            name_enc = 364
        elif name == 'Hyundai Grand i10 Nios Sportz':
            name_enc = 365
        elif name == 'Hyundai Grand i10 Sportz':
            name_enc = 366
        elif name == 'Hyundai Santa Fe 4WD AT':
            name_enc = 367
        elif name == 'Hyundai Santa Fe 4X4':
            name_enc = 368
        elif name == 'Hyundai Santro AT':
            name_enc = 369
        elif name == 'Hyundai Santro AT CNG':
            name_enc = 370
        elif name == 'Hyundai Santro Asta':
            name_enc = 371
        elif name == 'Hyundai Santro Era':
            name_enc = 372
        elif name == 'Hyundai Santro GLS I - Euro I':
            name_enc = 373
        elif name == 'Hyundai Santro GLS I - Euro II':
            name_enc = 374
        elif name == 'Hyundai Santro GS':
            name_enc = 375
        elif name == 'Hyundai Santro LE':
            name_enc = 376
        elif name == 'Hyundai Santro LE zipPlus':
            name_enc = 377
        elif name == 'Hyundai Santro LP zipPlus':
            name_enc = 378
        elif name == 'Hyundai Santro LS zipPlus':
            name_enc = 379
        elif name == 'Hyundai Santro Magna AMT BSIV':
            name_enc = 380
        elif name == 'Hyundai Santro Magna BSIV':
            name_enc = 381
        elif name == 'Hyundai Santro Magna CNG BSIV':
            name_enc = 383
        elif name == 'Hyundai Santro Sportz AMT':
            name_enc = 383
        elif name == 'Hyundai Santro Sportz BSIV':
            name_enc = 384
        elif name == 'Hyundai Santro Xing GL':
            name_enc = 385
        elif name == 'Hyundai Santro Xing GL PLUS CNG':
            name_enc = 386
        elif name == 'Hyundai Santro Xing GL Plus':
            name_enc = 387
        elif name == 'Hyundai Santro Xing GL Plus LPG':
            name_enc = 388
        elif name == 'Hyundai Santro Xing GLS':
            name_enc = 389
        elif name == 'Hyundai Santro Xing GLS Audio LPG':
            name_enc = 390
        elif name == 'Hyundai Santro Xing GLS CNG':
            name_enc = 391
        elif name == 'Hyundai Santro Xing XG':
            name_enc = 392
        elif name == 'Hyundai Santro Xing XG AT':
            name_enc = 393
        elif name == 'Hyundai Santro Xing XG eRLX Euro III':
            name_enc = 394
        elif name == 'Hyundai Santro Xing XK':
            name_enc = 395
        elif name == 'Hyundai Santro Xing XK (Non-AC)':
            name_enc = 396
        elif name == 'Hyundai Santro Xing XK eRLX EuroIII':
            name_enc = 397
        elif name == 'Hyundai Santro Xing XL AT eRLX Euro III':
            name_enc = 398
        elif name == 'Hyundai Santro Xing XL eRLX Euro III':
            name_enc = 399
        elif name == 'Hyundai Santro Xing XO':
            name_enc = 400
        elif name == 'Hyundai Santro Xing XS':
            name_enc = 401
        elif name == 'Hyundai Santro Xing XS eRLX Euro III':
            name_enc = 402
        elif name == 'Hyundai Sonata 2.4L AT':
            name_enc = 403
        elif name == 'Hyundai Sonata AT Leather':
            name_enc = 404
        elif name == 'Hyundai Sonata CRDi M/T':
            name_enc = 405
        elif name == 'Hyundai Tucson 2.0 e-VGT 2WD AT GL':
            name_enc = 406
        elif name == 'Hyundai Tucson 2.0 e-VGT 2WD MT':
            name_enc = 407
        elif name == 'Hyundai Tucson CRDi':
            name_enc = 408
        elif name == 'Hyundai Venue SX Opt Diesel':
            name_enc = 409
        elif name == 'Hyundai Venue SX Opt Turbo BSIV':
            name_enc = 410
        elif name == 'Hyundai Verna 1.4 CRDi':
            name_enc = 411
        elif name == 'Hyundai Verna 1.4 EX':
            name_enc = 412
        elif name == 'Hyundai Verna 1.4 VTVT':
            name_enc = 413
        elif name == 'Hyundai Verna 1.6 CRDI':
            name_enc = 414
        elif name == 'Hyundai Verna 1.6 CRDI SX Option':
            name_enc = 415
        elif name == 'Hyundai Verna 1.6 CRDi AT SX':
            name_enc = 416
        elif name == 'Hyundai Verna 1.6 CRDi SX':
            name_enc = 417
        elif name == 'Hyundai Verna 1.6 SX':
            name_enc = 418
        elif name == 'Hyundai Verna 1.6 SX CRDi (O)':
            name_enc = 419
        elif name == 'Hyundai Verna 1.6 SX VTVT':
            name_enc = 420
        elif name == 'Hyundai Verna 1.6 SX VTVT (O)':
            name_enc = 421
        elif name == 'Hyundai Verna 1.6 SX VTVT AT':
            name_enc = 422
        elif name == 'Hyundai Verna 1.6 VTVT':
            name_enc = 423
        elif name == 'Hyundai Verna 1.6 VTVT AT S Option':
            name_enc = 424
        elif name == 'Hyundai Verna 1.6 VTVT S':
            name_enc = 425
        elif name == 'Hyundai Verna 1.6 VTVT SX':
            name_enc = 426
        elif name == 'Hyundai Verna 1.6 Xi ABS':
            name_enc = 427
        elif name == 'Hyundai Verna 1.6 i ABS':
            name_enc = 428
        elif name == 'Hyundai Verna CRDi':
            name_enc = 429
        elif name == 'Hyundai Verna CRDi 1.6 AT EX':
            name_enc = 430
        elif name == 'Hyundai Verna CRDi 1.6 AT SX Option':
            name_enc = 431
        elif name == 'Hyundai Verna CRDi 1.6 EX':
            name_enc = 432
        elif name == 'Hyundai Verna CRDi 1.6 SX':
            name_enc = 433
        elif name == 'Hyundai Verna CRDi 1.6 SX Option':
            name_enc = 434
        elif name == 'Hyundai Verna CRDi ABS':
            name_enc = 435
        elif name == 'Hyundai Verna CRDi SX':
            name_enc = 436
        elif name == 'Hyundai Verna CRDi SX ABS':
            name_enc = 437
        elif name == 'Hyundai Verna SX':
            name_enc = 438
        elif name == 'Hyundai Verna SX AT Diesel':
            name_enc = 439
        elif name == 'Hyundai Verna SX CRDi AT':
            name_enc = 440
        elif name == 'Hyundai Verna SX Diesel':
            name_enc = 441
        elif name == 'Hyundai Verna Transform CRDi VGT ABS':
            name_enc = 442
        elif name == 'Hyundai Verna Transform CRDi VGT SX ABS':
            name_enc = 443
        elif name == 'Hyundai Verna Transform SX VTVT':
            name_enc = 444
        elif name == 'Hyundai Verna Transform VTVT':
            name_enc = 445
        elif name == 'Hyundai Verna VTVT 1.6 AT SX Option':
            name_enc = 446
        elif name == 'Hyundai Verna VTVT 1.6 SX':
            name_enc = 447
        elif name == 'Hyundai Verna XXi (Petrol)':
            name_enc = 448
        elif name == 'Hyundai Verna i (Petrol)':
            name_enc = 449
        elif name == 'Hyundai Xcent 1.1 CRDi Base':
            name_enc = 450
        elif name == 'Hyundai Xcent 1.1 CRDi S':
            name_enc = 451
        elif name == 'Hyundai Xcent 1.1 CRDi SX':
            name_enc = 452
        elif name == 'Hyundai Xcent 1.1 CRDi SX Option':
            name_enc = 453
        elif name == 'Hyundai Xcent 1.2 CRDi E':
            name_enc = 454
        elif name == 'Hyundai Xcent 1.2 CRDi S':
            name_enc = 455
        elif name == 'Hyundai Xcent 1.2 CRDi SX':
            name_enc = 456
        elif name == 'Hyundai Xcent 1.2 Kappa Base':
            name_enc = 457
        elif name == 'Hyundai Xcent 1.2 Kappa S':
            name_enc = 458
        elif name == 'Hyundai Xcent 1.2 Kappa SX':
            name_enc = 459
        elif name == 'Hyundai Xcent 1.2 VTVT E Plus':
            name_enc = 460
        elif name == 'Hyundai Xcent 1.2 VTVT S':
            name_enc = 461
        elif name == 'Hyundai Xcent 1.2 VTVT S AT':
            name_enc = 462
        elif name == 'Hyundai i10 Asta AT':
            name_enc = 463
        elif name == 'Hyundai i10 Era':
            name_enc = 464
        elif name == 'Hyundai i10 Era 1.1':
            name_enc = 465
        elif name == 'Hyundai i10 Era 1.1 iTech SE':
            name_enc = 466
        elif name == 'Hyundai i10 Magna':
            name_enc = 467
        elif name == 'Hyundai i10 Magna 1.1':
            name_enc = 468
        elif name == 'Hyundai i10 Magna 1.1 iTech SE':
            name_enc = 469
        elif name == 'Hyundai i10 Magna 1.1L':
            name_enc = 470
        elif name == 'Hyundai i10 Magna 1.2':
            name_enc = 471
        elif name == 'Hyundai i10 Magna 1.2 iTech SE':
            name_enc = 472
        elif name == 'Hyundai i10 Magna LPG':
            name_enc = 473
        elif name == 'Hyundai i10 Sportz':
            name_enc = 474
        elif name == 'Hyundai i10 Sportz 1.1L':
            name_enc = 475
        elif name == 'Hyundai i10 Sportz 1.2':
            name_enc = 476
        elif name == 'Hyundai i10 Sportz 1.2 AT':
            name_enc = 477
        elif name == 'Hyundai i10 Sportz AT':
            name_enc = 478
        elif name == 'Hyundai i20 1.2 Asta':
            name_enc = 479
        elif name == 'Hyundai i20 1.2 Asta Dual Tone':
            name_enc = 480
        elif name == 'Hyundai i20 1.2 Asta Option':
            name_enc = 481
        elif name == 'Hyundai i20 1.2 Era':
            name_enc = 482
        elif name == 'Hyundai i20 1.2 Magna':
            name_enc = 483
        elif name == 'Hyundai i20 1.2 Magna Executive':
            name_enc = 484
        elif name == 'Hyundai i20 1.2 Sportz':
            name_enc = 485
        elif name == 'Hyundai i20 1.2 Spotz':
            name_enc = 486
        elif name == 'Hyundai i20 1.4 Asta Option':
            name_enc = 487
        elif name == 'Hyundai i20 1.4 CRDi Asta':
            name_enc = 488
        elif name == 'Hyundai i20 1.4 CRDi Era':
            name_enc = 489
        elif name == 'Hyundai i20 1.4 CRDi Magna':
            name_enc = 490
        elif name == 'Hyundai i20 1.4 CRDi Sportz':
            name_enc = 491
        elif name == 'Hyundai i20 1.4 Magna ABS':
            name_enc = 492
        elif name == 'Hyundai i20 1.4 Magna Executive':
            name_enc = 493
        elif name == 'Hyundai i20 1.4 Sportz':
            name_enc = 494
        elif name == 'Hyundai i20 2015-2017 Magna 1.2':
            name_enc = 495
        elif name == 'Hyundai i20 2015-2017 Sportz Option 1.4 CRDi':
            name_enc = 496
        elif name == 'Hyundai i20 Active 1.2 S':
            name_enc = 497
        elif name == 'Hyundai i20 Active 1.2 SX':
            name_enc = 498
        elif name == 'Hyundai i20 Active 1.4 SX':
            name_enc = 499
        elif name == 'Hyundai i20 Active 1.4 SX with AVN':
            name_enc = 500
        elif name == 'Hyundai i20 Active S Diesel':
            name_enc = 501
        elif name == 'Hyundai i20 Active S Petrol':
            name_enc = 502
        elif name == 'Hyundai i20 Active SX Petrol':
            name_enc = 503
        elif name == 'Hyundai i20 Asta':
            name_enc = 504
        elif name == 'Hyundai i20 Asta (o)':
            name_enc = 505
        elif name == 'Hyundai i20 Asta (o) 1.4 CRDi (Diesel)':
            name_enc = 506
        elif name == 'Hyundai i20 Asta 1.2':
            name_enc = 507
        elif name == 'Hyundai i20 Asta 1.4 CRDi':
            name_enc = 508
        elif name == 'Hyundai i20 Asta 1.4 CRDi (Diesel)':
            name_enc = 509
        elif name == 'Hyundai i20 Asta Option 1.2':
            name_enc = 510
        elif name == 'Hyundai i20 Asta Option 1.4 CRDi':
            name_enc = 511
        elif name == 'Hyundai i20 Magna':
            name_enc = 512
        elif name == 'Hyundai i20 Magna 1.2':
            name_enc = 513
        elif name == 'Hyundai i20 Magna 1.4 CRDi':
            name_enc = 514
        elif name == 'Hyundai i20 Magna 1.4 CRDi (Diesel)':
            name_enc = 515
        elif name == 'Hyundai i20 Magna Optional 1.2':
            name_enc = 516
        elif name == 'Hyundai i20 Magna Optional 1.4 CRDi':
            name_enc = 517
        elif name == 'Hyundai i20 Sportz 1.2':
            name_enc = 518
        elif name == 'Hyundai i20 Sportz 1.4 CRDi':
            name_enc = 519
        elif name == 'Hyundai i20 Sportz Option 1.2':
            name_enc = 520
        elif name == 'Hyundai i20 Sportz Petrol':
            name_enc = 521

    elif brand == 'Mahindra':
        brand_enc = 17
        if name == 'Mahindra Alturas G4 4X2 AT BSIV':
            name_enc = 522
        elif name == 'Mahindra Bolero 2011-2019 SLE':
            name_enc = 523
        elif name == 'Mahindra Bolero 2011-2019 SLX':
            name_enc = 524
        elif name == 'Mahindra Bolero 2011-2019 SLX 2WD BSIII':
            name_enc = 525
        elif name == 'Mahindra Bolero B4':
            name_enc = 526
        elif name == 'Mahindra Bolero B6':
            name_enc = 527
        elif name == 'Mahindra Bolero DI':
            name_enc = 528
        elif name == 'Mahindra Bolero DI DX 7 Seater':
            name_enc = 529
        elif name == 'Mahindra Bolero DI DX 8 Seater':
            name_enc = 530
        elif name == 'Mahindra Bolero Power Plus LX':
            name_enc = 531
        elif name == 'Mahindra Bolero Power Plus Plus AC BSIV PS':
            name_enc = 532
        elif name == 'Mahindra Bolero Power Plus Plus Non AC BSIV PS':
            name_enc = 533
        elif name == 'Mahindra Bolero Power Plus SLE':
            name_enc = 534
        elif name == 'Mahindra Bolero Power Plus SLX':
            name_enc = 535
        elif name == 'Mahindra Bolero Power Plus ZLX':
            name_enc = 536
        elif name == 'Mahindra Bolero SLE':
            name_enc = 537
        elif name == 'Mahindra Bolero SLE BSIII':
            name_enc = 538
        elif name == 'Mahindra Bolero SLX':
            name_enc = 539
        elif name == 'Mahindra Bolero SLX 2WD':
            name_enc = 540
        elif name == 'Mahindra Bolero SLX 2WD BSIII':
            name_enc = 541
        elif name == 'Mahindra Bolero SLX 4WD BSIII':
            name_enc = 542
        elif name == 'Mahindra Ingenio CRDe':
            name_enc = 543
        elif name == 'Mahindra Jeep CJ 500 DI':
            name_enc = 544
        elif name == 'Mahindra Jeep CL 500 MDI':
            name_enc = 545
        elif name == 'Mahindra Jeep Classic':
            name_enc = 546
        elif name == 'Mahindra Jeep MM 540':
            name_enc = 547
        elif name == 'Mahindra Jeep MM 550 XDB':
            name_enc = 548
        elif name == 'Mahindra Jeep MM 775 XDB':
            name_enc = 549
        elif name == 'Mahindra KUV 100 D75 K2':
            name_enc = 550
        elif name == 'Mahindra KUV 100 D75 K4 Plus 5Str':
            name_enc = 551
        elif name == 'Mahindra KUV 100 D75 K6 Plus':
            name_enc = 552
        elif name == 'Mahindra KUV 100 G80 K2':
            name_enc = 553
        elif name == 'Mahindra KUV 100 G80 K4 Plus':
            name_enc = 554
        elif name == 'Mahindra KUV 100 mFALCON D75 K6':
            name_enc = 555
        elif name == 'Mahindra KUV 100 mFALCON D75 K8':
            name_enc = 556
        elif name == 'Mahindra KUV 100 mFALCON D75 K8 AW':
            name_enc = 557
        elif name == 'Mahindra KUV 100 mFALCON G80 K2':
            name_enc = 558
        elif name == 'Mahindra KUV 100 mFALCON G80 K2 Plus':
            name_enc = 559
        elif name == 'Mahindra KUV 100 mFALCON G80 K8 5str':
            name_enc = 560
        elif name == 'Mahindra Marazzo M2 8Str':
            name_enc = 561
        elif name == 'Mahindra Marazzo M4':
            name_enc = 562
        elif name == 'Mahindra Marazzo M8 8Str':
            name_enc = 563
        elif name == 'Mahindra NuvoSport N8':
            name_enc = 564
        elif name == 'Mahindra Quanto C4':
            name_enc = 565
        elif name == 'Mahindra Quanto C6':
            name_enc = 566
        elif name == 'Mahindra Quanto C8':
            name_enc = 567
        elif name == 'Mahindra Renault Logan 1.4 GLX Petrol':
            name_enc = 568
        elif name == 'Mahindra Renault Logan 1.5 DLE Diesel':
            name_enc = 569
        elif name == 'Mahindra Renault Logan 1.5 DLS':
            name_enc = 570
        elif name == 'Mahindra Renault Logan 1.5 DLX Diesel':
            name_enc = 571
        elif name == 'Mahindra Renault Logan 1.6 Petrol GLSX':
            name_enc = 572
        elif name == 'Mahindra Scorpio 1.99 S10':
            name_enc = 573
        elif name == 'Mahindra Scorpio 1.99 S4':
            name_enc = 574
        elif name == 'Mahindra Scorpio 1.99 S6 Plus':
            name_enc = 575
        elif name == 'Mahindra Scorpio 2.6 CRDe':
            name_enc = 576
        elif name == 'Mahindra Scorpio 2.6 CRDe SLE':
            name_enc = 577
        elif name == 'Mahindra Scorpio 2.6 SLX CRDe':
            name_enc = 578
        elif name == 'Mahindra Scorpio 2.6 SLX Turbo 7 Seater':
            name_enc = 579
        elif name == 'Mahindra Scorpio 2.6 Turbo 7 Str':
            name_enc = 580
        elif name == 'Mahindra Scorpio 2.6 Turbo 9 Str':
            name_enc = 581
        elif name == 'Mahindra Scorpio BSIV':
            name_enc = 582
        elif name == 'Mahindra Scorpio EX':
            name_enc = 583
        elif name == 'Mahindra Scorpio LX':
            name_enc = 584
        elif name == 'Mahindra Scorpio LX BSIV':
            name_enc = 585
        elif name == 'Mahindra Scorpio M2DI':
            name_enc = 586
        elif name == 'Mahindra Scorpio REV 116':
            name_enc = 587
        elif name == 'Mahindra Scorpio S10 7 Seater':
            name_enc = 588
        elif name == 'Mahindra Scorpio S11 BSIV':
            name_enc = 589
        elif name == 'Mahindra Scorpio S2 7 Seater':
            name_enc = 590
        elif name == 'Mahindra Scorpio S2 9 Seater':
            name_enc = 591
        elif name == 'Mahindra Scorpio S4 4WD':
            name_enc = 592
        elif name == 'Mahindra Scorpio S5 BSIV':
            name_enc = 593
        elif name == 'Mahindra Scorpio S6 Plus 7 Seater':
            name_enc = 594
        elif name == 'Mahindra Scorpio S7 140 BSIV':
            name_enc = 595
        elif name == 'Mahindra Scorpio S9 BSIV':
            name_enc = 596
        elif name == 'Mahindra Scorpio SLE BS IV':
            name_enc = 597
        elif name == 'Mahindra Scorpio SLE BS IV':
            name_enc = 598
        elif name == 'Mahindra Scorpio SLE BSIII':
            name_enc = 599
        elif name == 'Mahindra Scorpio SLE BSIV':
            name_enc = 600
        elif name == 'Mahindra Scorpio SLX 2.6 Turbo 8 Str':
            name_enc = 601
        elif name == 'Mahindra Scorpio VLS 2.2 mHawk':
            name_enc = 602
        elif name == 'Mahindra Scorpio VLS AT 2.2 mHAWK':
            name_enc = 603
        elif name == 'Mahindra Scorpio VLX 2.2 mHawk Airbag BSIV':
            name_enc = 604
        elif name == 'Mahindra Scorpio VLX 2WD ABS AT BSIII':
            name_enc = 605
        elif name == 'Mahindra Scorpio VLX 2WD AIRBAG BSIV':
            name_enc = 606
        elif name == 'Mahindra Scorpio VLX 2WD AIRBAG SE BSIV':
            name_enc = 607
        elif name == 'Mahindra Scorpio VLX 2WD AT BSIV':
            name_enc = 608
        elif name == 'Mahindra Scorpio VLX 2WD BSIII':
            name_enc = 609
        elif name == 'Mahindra Scorpio VLX 2WD BSIV':
            name_enc = 610
        elif name == 'Mahindra Scorpio VLX AT 2WD BSIII':
            name_enc = 611
        elif name == 'Mahindra Supro VX 8 Str':
            name_enc = 612
        elif name == 'Mahindra TUV 300 Plus P4':
            name_enc = 613
        elif name == 'Mahindra TUV 300 T10':
            name_enc = 614
        elif name == 'Mahindra TUV 300 T10 Dual Tone':
            name_enc = 615
        elif name == 'Mahindra TUV 300 T4':
            name_enc = 616
        elif name == 'Mahindra TUV 300 T4 Plus':
            name_enc = 617
        elif name == 'Mahindra TUV 300 T6 Plus':
            name_enc = 618
        elif name == 'Mahindra TUV 300 T8':
            name_enc = 619
        elif name == 'Mahindra TUV 300 T8 AMT':
            name_enc = 620
        elif name == 'Mahindra TUV 300 mHAWK100 T8':
            name_enc = 621
        elif name == 'Mahindra Thar 4X2':
            name_enc = 622
        elif name == 'Mahindra Thar 4X4':
            name_enc = 623
        elif name == 'Mahindra Thar CRDe':
            name_enc = 624
        elif name == 'Mahindra Thar CRDe ABS':
            name_enc = 625
        elif name == 'Mahindra Thar CRDe AC':
            name_enc = 626
        elif name == 'Mahindra Thar DI 4X2':
            name_enc = 627
        elif name == 'Mahindra Thar DI 4X4 PS':
            name_enc = 628
        elif name == 'Mahindra Verito 1.5 D2 BSIII':
            name_enc = 629
        elif name == 'Mahindra Verito 1.5 D2 BSIV':
            name_enc = 630
        elif name == 'Mahindra Verito 1.5 D4 BSIV':
            name_enc = 631
        elif name == 'Mahindra Verito 1.5 D6 BSIII':
            name_enc = 632
        elif name == 'Mahindra Verito Vibe 1.5 dCi D4':
            name_enc = 633
        elif name == 'Mahindra Verito Vibe 1.5 dCi D6':
            name_enc = 634
        elif name == 'Mahindra XUV300 W8 Option':
            name_enc = 635
        elif name == 'Mahindra XUV300 W8 Option Diesel BSIV':
            name_enc = 636
        elif name == 'Mahindra XUV500 AT W10 1.99 mHawk':
            name_enc = 637
        elif name == 'Mahindra XUV500 AT W10 AWD':
            name_enc = 638
        elif name == 'Mahindra XUV500 AT W10 FWD':
            name_enc = 639
        elif name == 'Mahindra XUV500 AT W6 2WD':
            name_enc = 640
        elif name == 'Mahindra XUV500 AT W8 FWD':
            name_enc = 641
        elif name == 'Mahindra XUV500 W10 1.99 mHawk':
            name_enc = 642
        elif name == 'Mahindra XUV500 W10 2WD':
            name_enc = 643
        elif name == 'Mahindra XUV500 W10 AWD':
            name_enc = 644
        elif name == 'Mahindra XUV500 W11 AT BSIV':
            name_enc = 645
        elif name == 'Mahindra XUV500 W11 Option AT AWD':
            name_enc = 646
        elif name == 'Mahindra XUV500 W11 Option AWD':
            name_enc = 647
        elif name == 'Mahindra XUV500 W5 BSIV':
            name_enc = 648
        elif name == 'Mahindra XUV500 W6 1.99 mHawk':
            name_enc = 649
        elif name == 'Mahindra XUV500 W6 2WD':
            name_enc = 650
        elif name == 'Mahindra XUV500 W7':
            name_enc = 651
        elif name == 'Mahindra XUV500 W7 AT BSIV':
            name_enc = 652
        elif name == 'Mahindra XUV500 W7 BSIV':
            name_enc = 653
        elif name == 'Mahindra XUV500 W8 2WD':
            name_enc = 654
        elif name == 'Mahindra XUV500 W8 4WD':
            name_enc = 655
        elif name == 'Mahindra Xylo Celebration Edition BSIV':
            name_enc = 656
        elif name == 'Mahindra Xylo D2':
            name_enc = 657
        elif name == 'Mahindra Xylo D2 BS IV':
            name_enc = 658
        elif name == 'Mahindra Xylo D2 BSIV':
            name_enc = 659
        elif name == 'Mahindra Xylo D2 Maxx':
            name_enc = 660
        elif name == 'Mahindra Xylo D4':
            name_enc = 661
        elif name == 'Mahindra Xylo D4 BSIV':
            name_enc = 662
        elif name == 'Mahindra Xylo E4':
            name_enc = 663
        elif name == 'Mahindra Xylo E4 8S':
            name_enc = 664
        elif name == 'Mahindra Xylo E4 ABS BS IV':
            name_enc = 665
        elif name == 'Mahindra Xylo E4 BS III':
            name_enc = 666
        elif name == 'Mahindra Xylo E6':
            name_enc = 667
        elif name == 'Mahindra Xylo E8':
            name_enc = 668
        elif name == 'Mahindra Xylo E8 ABS Airbag BSIV':
            name_enc = 669
        elif name == 'Mahindra Xylo E9':
            name_enc = 670
        elif name == 'Mahindra Xylo H4':
            name_enc = 671
        elif name == 'Mahindra Xylo H4 ABS':
            name_enc = 672
        elif name == 'Mahindra Xylo H8 ABS with Airbags':
            name_enc = 673

    elif brand == 'Maruti':
        brand_enc = 18
        if name == 'Maruti 800 AC':
            name_enc = 674
        elif name == 'Maruti 800 AC BSII':
            name_enc = 675
        elif name == 'Maruti 800 AC BSIII':
            name_enc = 676
        elif name == 'Maruti 800 AC Uniq':
            name_enc = 677
        elif name == 'Maruti 800 DUO AC LPG':
            name_enc = 678
        elif name == 'Maruti 800 DX':
            name_enc = 679
        elif name == 'Maruti 800 EX':
            name_enc = 680
        elif name == 'Maruti 800 Std':
            name_enc = 681
        elif name == 'Maruti 800 Std BSII':
            name_enc = 682
        elif name == 'Maruti 800 Std BSIII':
            name_enc = 683
        elif name == 'Maruti 800 Std MPFi':
            name_enc = 684
        elif name == 'Maruti A-Star AT VXI':
            name_enc = 685
        elif name == 'Maruti A-Star Lxi':
            name_enc = 686
        elif name == 'Maruti A-Star Vxi':
            name_enc = 687
        elif name == 'Maruti Alto 800 Base':
            name_enc = 688
        elif name == 'Maruti Alto 800 CNG LXI':
            name_enc = 689
        elif name == 'Maruti Alto 800 CNG LXI Optional':
            name_enc = 690
        elif name == 'Maruti Alto 800 LX':
            name_enc = 691
        elif name == 'Maruti Alto 800 LXI':
            name_enc = 692
        elif name == 'Maruti Alto 800 LXI Airbag':
            name_enc = 693
        elif name == 'Maruti Alto 800 LXI CNG':
            name_enc = 694
        elif name == 'Maruti Alto 800 LXI Opt BSIV':
            name_enc = 695
        elif name == 'Maruti Alto 800 LXI Optional':
            name_enc = 696
        elif name == 'Maruti Alto 800 Std Optional':
            name_enc = 697
        elif name == 'Maruti Alto 800 VXI':
            name_enc = 698
        elif name == 'Maruti Alto Green LXi (CNG)':
            name_enc = 699
        elif name == 'Maruti Alto K10 2010-2014 VXI':
            name_enc = 700
        elif name == 'Maruti Alto K10 LX':
            name_enc = 701
        elif name == 'Maruti Alto K10 LXI':
            name_enc = 702
        elif name == 'Maruti Alto K10 LXI CNG':
            name_enc = 703
        elif name == 'Maruti Alto K10 LXI CNG Optional':
            name_enc = 704
        elif name == 'Maruti Alto K10 VXI':
            name_enc = 705
        elif name == 'Maruti Alto K10 VXI AGS':
            name_enc = 706
        elif name == 'Maruti Alto K10 VXI AGS Optional':
            name_enc = 707
        elif name == 'Maruti Alto K10 VXI Airbag':
            name_enc = 708
        elif name == 'Maruti Alto K10 VXI Optional':
            name_enc = 709
        elif name == 'Maruti Alto LX':
            name_enc = 710
        elif name == 'Maruti Alto LX BSIII':
            name_enc = 711
        elif name == 'Maruti Alto LXI':
            name_enc = 712
        elif name == 'Maruti Alto LXi':
            name_enc = 713
        elif name == 'Maruti Alto LXi BSII':
            name_enc = 714
        elif name == 'Maruti Alto LXi BSIII':
            name_enc = 715
        elif name == 'Maruti Alto STD':
            name_enc = 716
        elif name == 'Maruti Alto VXi':
            name_enc = 717
        elif name == 'Maruti Baleno Alpha':
            name_enc = 718
        elif name == 'Maruti Baleno Alpha 1.2':
            name_enc = 719
        elif name == 'Maruti Baleno Alpha 1.3':
            name_enc = 720
        elif name == 'Maruti Baleno Alpha CVT':
            name_enc = 721
        elif name == 'Maruti Baleno Delta 1.2':
            name_enc = 722
        elif name == 'Maruti Baleno Delta 1.3':
            name_enc = 723
        elif name == 'Maruti Baleno Delta Automatic':
            name_enc = 724
        elif name == 'Maruti Baleno Delta Diesel':
            name_enc = 725
        elif name == 'Maruti Baleno RS 1.0 Petrol':
            name_enc = 726
        elif name == 'Maruti Baleno Sigma 1.2':
            name_enc = 727
        elif name == 'Maruti Baleno Vxi':
            name_enc = 728
        elif name == 'Maruti Baleno Zeta':
            name_enc = 729
        elif name == 'Maruti Baleno Zeta 1.2':
            name_enc = 730
        elif name == 'Maruti Baleno Zeta 1.3':
            name_enc = 731
        elif name == 'Maruti Baleno Zeta Automatic':
            name_enc = 732
        elif name == 'Maruti Celerio Green VXI':
            name_enc = 733
        elif name == 'Maruti Celerio LXI MT BSIV':
            name_enc = 734
        elif name == 'Maruti Celerio VDi':
            name_enc = 735
        elif name == 'Maruti Celerio VXI':
            name_enc = 736
        elif name == 'Maruti Celerio VXI AMT BSIV':
            name_enc = 737
        elif name == 'Maruti Celerio VXI AT':
            name_enc = 738
        elif name == 'Maruti Celerio VXI Optional':
            name_enc = 739
        elif name == 'Maruti Celerio X ZXI BSIV':
            name_enc = 740
        elif name == 'Maruti Celerio ZDi':
            name_enc = 741
        elif name == 'Maruti Celerio ZXI':
            name_enc = 742
        elif name == 'Maruti Celerio ZXI AMT BSIV':
            name_enc = 743
        elif name == 'Maruti Celerio ZXI AT':
            name_enc = 744
        elif name == 'Maruti Celerio ZXI MT BSIV':
            name_enc = 745
        elif name == 'Maruti Celerio ZXI Optional AMT BSIV':
            name_enc = 746
        elif name == 'Maruti Ciaz 1.3 Delta':
            name_enc = 747
        elif name == 'Maruti Ciaz 1.4 AT Zeta':
            name_enc = 748
        elif name == 'Maruti Ciaz 1.4 Alpha':
            name_enc = 749
        elif name == 'Maruti Ciaz 1.4 Delta':
            name_enc = 750
        elif name == 'Maruti Ciaz 1.4 Zeta':
            name_enc = 751
        elif name == 'Maruti Ciaz S 1.3':
            name_enc = 752
        elif name == 'Maruti Ciaz Sigma BSIV':
            name_enc = 753
        elif name == 'Maruti Ciaz VDI SHVS':
            name_enc = 754
        elif name == 'Maruti Ciaz VDi':
            name_enc = 755
        elif name == 'Maruti Ciaz VDi Option SHVS':
            name_enc = 756
        elif name == 'Maruti Ciaz VDi Plus':
            name_enc = 757
        elif name == 'Maruti Ciaz VDi Plus SHVS':
            name_enc = 758
        elif name == 'Maruti Ciaz VXi':
            name_enc = 759
        elif name == 'Maruti Ciaz VXi Plus':
            name_enc = 760
        elif name == 'Maruti Ciaz ZDi':
            name_enc = 761
        elif name == 'Maruti Ciaz ZDi Plus':
            name_enc = 762
        elif name == 'Maruti Ciaz ZDi Plus SHVS':
            name_enc = 763
        elif name == 'Maruti Ciaz ZDi SHVS':
            name_enc = 764
        elif name == 'Maruti Ciaz ZXi':
            name_enc = 765
        elif name == 'Maruti Ciaz ZXi Plus':
            name_enc = 766
        elif name == 'Maruti Ciaz Zeta BSIV':
            name_enc = 767
        elif name == 'Maruti Eeco 5 STR With AC Plus HTR CNG':
            name_enc = 768
        elif name == 'Maruti Eeco 5 Seater AC BSIV':
            name_enc = 769
        elif name == 'Maruti Eeco 5 Seater Standard BSIV':
            name_enc = 770
        elif name == 'Maruti Eeco 7 Seater Standard BSIV':
            name_enc = 771
        elif name == 'Maruti Eeco CNG 5 Seater AC BSIV':
            name_enc = 772
        elif name == 'Maruti Eeco Smiles 5 Seater AC':
            name_enc = 773
        elif name == 'Maruti Ertiga 1.5 VDI':
            name_enc = 774
        elif name == 'Maruti Ertiga BSIV VXI AT':
            name_enc = 775
        elif name == 'Maruti Ertiga BSIV ZXI':
            name_enc = 776
        elif name == 'Maruti Ertiga SHVS LDI':
            name_enc = 777
        elif name == 'Maruti Ertiga SHVS LDI Option':
            name_enc = 778
        elif name == 'Maruti Ertiga SHVS VDI':
            name_enc = 779
        elif name == 'Maruti Ertiga SHVS ZDI':
            name_enc = 780
        elif name == 'Maruti Ertiga SHVS ZDI Plus':
            name_enc = 781
        elif name == 'Maruti Ertiga VDI':
            name_enc = 782
        elif name == 'Maruti Ertiga VDI Limited Edition':
            name_enc = 783
        elif name == 'Maruti Ertiga VXI':
            name_enc = 784
        elif name == 'Maruti Ertiga VXI ABS':
            name_enc = 785
        elif name == 'Maruti Ertiga VXI CNG':
            name_enc = 786
        elif name == 'Maruti Ertiga VXI Petrol':
            name_enc = 787
        elif name == 'Maruti Ertiga ZDI':
            name_enc = 788
        elif name == 'Maruti Ertiga ZDI Plus':
            name_enc = 789
        elif name == 'Maruti Ertiga ZXI':
            name_enc = 790
        elif name == 'Maruti Ertiga ZXI AT Petrol':
            name_enc = 791
        elif name == 'Maruti Esteem AX':
            name_enc = 792
        elif name == 'Maruti Esteem Lxi':
            name_enc = 793
        elif name == 'Maruti Esteem Lxi - BSIII':
            name_enc = 794
        elif name == 'Maruti Esteem VX':
            name_enc = 795
        elif name == 'Maruti Esteem Vxi':
            name_enc = 796
        elif name == 'Maruti Esteem Vxi - BSIII':
            name_enc = 797
        elif name == 'Maruti Estilo LXI':
            name_enc = 798
        elif name == 'Maruti Grand Vitara MT':
            name_enc = 799
        elif name == 'Maruti Gypsy E MG410W ST':
            name_enc = 800
        elif name == 'Maruti Gypsy King HT BSIV':
            name_enc = 801
        elif name == 'Maruti Gypsy King Hard Top':
            name_enc = 802
        elif name == 'Maruti Gypsy King Hard Top Ambulance BSIV':
            name_enc = 803
        elif name == 'Maruti Ignis 1.2 AMT Alpha BSIV':
            name_enc = 804
        elif name == 'Maruti Ignis 1.2 AMT Delta BSIV':
            name_enc = 805
        elif name == 'Maruti Ignis 1.2 Alpha BSIV':
            name_enc = 806
        elif name == 'Maruti Ignis 1.2 Delta BSIV':
            name_enc = 807
        elif name == 'Maruti Ignis 1.2 Sigma BSIV':
            name_enc = 808
        elif name == 'Maruti Ignis 1.2 Zeta BSIV':
            name_enc = 809
        elif name == 'Maruti Ignis 1.3 Delta':
            name_enc = 810
        elif name == 'Maruti Omni 5 Str STD':
            name_enc = 811
        elif name == 'Maruti Omni 5 Str STD LPG':
            name_enc = 812
        elif name == 'Maruti Omni 8 Seater BSII':
            name_enc = 813
        elif name == 'Maruti Omni 8 Seater BSIV':
            name_enc = 814
        elif name == 'Maruti Omni BSIII 8-STR W/ IMMOBILISER':
            name_enc = 815
        elif name == 'Maruti Omni CNG':
            name_enc = 816
        elif name == 'Maruti Omni E 8 Str STD':
            name_enc = 817
        elif name == 'Maruti Omni E MPI STD BS IV':
            name_enc = 818
        elif name == 'Maruti Omni LPG CARGO BSIII W IMMOBILISER':
            name_enc = 819
        elif name == 'Maruti Omni LPG STD BSIV':
            name_enc = 820
        elif name == 'Maruti Omni MPI STD BSIV':
            name_enc = 821
        elif name == 'Maruti Omni Maruti Omni MPI STD BSIII 5-STR W/ IMMOBILISER':
            name_enc = 822
        elif name == 'Maruti Ritz LDi':
            name_enc = 823
        elif name == 'Maruti Ritz LXI':
            name_enc = 824
        elif name == 'Maruti Ritz LXi':
            name_enc = 825
        elif name == 'Maruti Ritz VDI (ABS) BS IV':
            name_enc = 826
        elif name == 'Maruti Ritz VDi':
            name_enc = 827
        elif name == 'Maruti Ritz VXI':
            name_enc = 828
        elif name == 'Maruti Ritz VXi':
            name_enc = 829
        elif name == 'Maruti S-Cross Alpha DDiS 200 SH':
            name_enc = 830
        elif name == 'Maruti S-Cross Delta DDiS 200 SH':
            name_enc = 831
        elif name == 'Maruti S-Cross Facelift':
            name_enc = 832
        elif name == 'Maruti S-Cross Sigma DDiS 200 SH':
            name_enc = 833
        elif name == 'Maruti S-Cross Zeta DDiS 200 SH':
            name_enc = 834
        elif name == 'Maruti S-Presso VXI Plus':
            name_enc = 835
        elif name == 'Maruti SX4 Celebration Diesel':
            name_enc = 836
        elif name == 'Maruti SX4 Celebration Petrol':
            name_enc = 837
        elif name == 'Maruti SX4 S Cross DDiS 320 Delta':
            name_enc = 838
        elif name == 'Maruti SX4 S Cross DDiS 320 Zeta':
            name_enc = 839
        elif name == 'Maruti SX4 VDI':
            name_enc = 840
        elif name == 'Maruti SX4 Vxi BSIII':
            name_enc = 841
        elif name == 'Maruti SX4 Vxi BSIV':
            name_enc = 842
        elif name == 'Maruti SX4 ZDI':
            name_enc = 843
        elif name == 'Maruti SX4 ZDI Leather':
            name_enc = 844
        elif name == 'Maruti SX4 ZXI AT':
            name_enc = 845
        elif name == 'Maruti SX4 ZXI MT BSIV':
            name_enc = 846
        elif name == 'Maruti SX4 Zxi BSIII':
            name_enc = 847
        elif name == 'Maruti SX4 Zxi with Leather BSIII':
            name_enc = 848
        elif name == 'Maruti Swift 1.2 DLX':
            name_enc = 849
        elif name == 'Maruti Swift 1.3 DLX':
            name_enc = 850
        elif name == 'Maruti Swift 1.3 LXI':
            name_enc = 851
        elif name == 'Maruti Swift 1.3 VXI ABS':
            name_enc = 852
        elif name == 'Maruti Swift 1.3 VXi':
            name_enc = 853
        elif name == 'Maruti Swift AMT VXI':
            name_enc = 854
        elif name == 'Maruti Swift DDiS LDI':
            name_enc = 855
        elif name == 'Maruti Swift DDiS VDI':
            name_enc = 856
        elif name == 'Maruti Swift Dzire 1.2 Vxi BSIV':
            name_enc = 857
        elif name == 'Maruti Swift Dzire AMT VDI':
            name_enc = 858
        elif name == 'Maruti Swift Dzire AMT VXI':
            name_enc = 859
        elif name == 'Maruti Swift Dzire AMT ZXI':
            name_enc = 860
        elif name == 'Maruti Swift Dzire AMT ZXI Plus BS IV':
            name_enc = 861
        elif name == 'Maruti Swift Dzire LDI':
            name_enc = 862
        elif name == 'Maruti Swift Dzire LDI Optional':
            name_enc = 863
        elif name == 'Maruti Swift Dzire LDIX Limited Edition':
            name_enc = 864
        elif name == 'Maruti Swift Dzire LDi':
            name_enc = 965
        elif name == 'Maruti Swift Dzire LXI':
            name_enc = 866
        elif name == 'Maruti Swift Dzire LXI Option':
            name_enc = 867
        elif name == 'Maruti Swift Dzire LXi':
            name_enc = 868
        elif name == 'Maruti Swift Dzire Tour LDI':
            name_enc = 869
        elif name == 'Maruti Swift Dzire VDI':
            name_enc = 870
        elif name == 'Maruti Swift Dzire VDI Optional':
            name_enc = 871
        elif name == 'Maruti Swift Dzire VDi':
            name_enc = 872
        elif name == 'Maruti Swift Dzire VXI':
            name_enc = 873
        elif name == 'Maruti Swift Dzire VXI 1.2 BS IV':
            name_enc = 874
        elif name == 'Maruti Swift Dzire VXi':
            name_enc = 875
        elif name == 'Maruti Swift Dzire Vdi BSIV':
            name_enc = 876
        elif name == 'Maruti Swift Dzire ZDI':
            name_enc = 878
        elif name == 'Maruti Swift Dzire ZXI': 
            name_enc = 879
        elif name == 'Maruti Swift Dzire ZXI 1.2 BS IV':
            name_enc = 880
        elif name == 'Maruti Swift Dzire ZXI Plus':
            name_enc = 881
        elif name == 'Maruti Swift Glam':
            name_enc = 882
        elif name == 'Maruti Swift LDI':
            name_enc = 883
        elif name == 'Maruti Swift LDI BSIV':
            name_enc = 884
        elif name == 'Maruti Swift LDI Optional':
            name_enc = 885
        elif name == 'Maruti Swift LXI':
            name_enc = 886
        elif name == 'Maruti Swift LXI Option':
            name_enc = 887
        elif name == 'Maruti Swift LXi BSIV':
            name_enc = 888
        elif name == 'Maruti Swift Ldi BSIII':
            name_enc = 889
        elif name == 'Maruti Swift Ldi BSIV':
            name_enc = 890
        elif name == 'Maruti Swift Star VDI':
            name_enc = 891
        elif name == 'Maruti Swift VDI':
            name_enc = 892
        elif name == 'Maruti Swift VDI BSIV':
            name_enc = 893
        elif name == 'Maruti Swift VDI Optional':
            name_enc = 894
        elif name == 'Maruti Swift VDi BSIII W/ ABS':
            name_enc = 895
        elif name == 'Maruti Swift VVT VXI':
            name_enc = 896
        elif name == 'Maruti Swift VVT ZXI':
            name_enc = 897
        elif name == 'Maruti Swift VXI':
            name_enc = 898
        elif name == 'Maruti Swift VXI BSIII':
            name_enc = 898
        elif name == 'Maruti Swift VXI BSIV':
            name_enc = 899
        elif name == 'Maruti Swift VXI Deca':
            name_enc = 900
        elif name == 'Maruti Swift VXI Optional':
            name_enc = 901
        elif name == 'Maruti Swift VXI with ABS':
            name_enc = 902
        elif name == 'Maruti Swift VXi BSIV':
            name_enc = 903
        elif name == 'Maruti Swift Vdi BSIII':
            name_enc = 904
        elif name == 'Maruti Swift ZDI':
            name_enc = 905
        elif name == 'Maruti Swift ZDI Plus':
            name_enc = 906
        elif name == 'Maruti Swift ZDi':
            name_enc = 907
        elif name == 'Maruti Swift ZDi BSIV':
            name_enc = 908
        elif name == 'Maruti Swift ZXI':
            name_enc = 909
        elif name == 'Maruti Swift ZXI ABS':
            name_enc = 910
        elif name == 'Maruti Swift ZXI BSIV':
            name_enc = 911
        elif name == 'Maruti Swift ZXI Plus':
            name_enc = 912
        elif name == 'Maruti Swift ZXi BSIV':
            name_enc = 913
        elif name == 'Maruti Vitara Brezza LDi':
            name_enc = 914
        elif name == 'Maruti Vitara Brezza LDi Option':
            name_enc = 915
        elif name == 'Maruti Vitara Brezza VDi':
            name_enc = 916
        elif name == 'Maruti Vitara Brezza VDi Option':
            name_enc = 917
        elif name == 'Maruti Vitara Brezza ZDi':
            name_enc = 918
        elif name == 'Maruti Vitara Brezza ZDi Plus':
            name_enc = 919
        elif name == 'Maruti Vitara Brezza ZDi Plus AMT':
            name_enc = 920
        elif name == 'Maruti Vitara Brezza ZDi Plus AMT Dual Tone':
            name_enc = 921
        elif name == 'Maruti Vitara Brezza ZDi Plus Dual Tone':
            name_enc = 922
        elif name == 'Maruti Wagon R AMT VXI':
            name_enc = 923
        elif name == 'Maruti Wagon R AMT VXI Option':
            name_enc = 924
        elif name == 'Maruti Wagon R AX':
            name_enc = 925
        elif name == 'Maruti Wagon R CNG LXI':
            name_enc = 926
        elif name == 'Maruti Wagon R DUO LPG':
            name_enc = 927
        elif name == 'Maruti Wagon R Duo Lxi':
            name_enc = 928
        elif name == 'Maruti Wagon R LX':
            name_enc = 929
        elif name == 'Maruti Wagon R LX BS IV':
            name_enc = 930
        elif name == 'Maruti Wagon R LX BSIII':
            name_enc = 931
        elif name == 'Maruti Wagon R LX Minor':
            name_enc = 932
        elif name == 'Maruti Wagon R LXI':
            name_enc = 933
        elif name == 'Maruti Wagon R LXI BS IV':
            name_enc = 934
        elif name == 'Maruti Wagon R LXI BSIII':
            name_enc = 935
        elif name == 'Maruti Wagon R LXI CNG':
            name_enc = 936
        elif name == 'Maruti Wagon R LXI DUO BS IV':
            name_enc = 937
        elif name == 'Maruti Wagon R LXI DUO BSIII':
            name_enc = 938
        elif name == 'Maruti Wagon R LXI LPG BSIV':
            name_enc = 939
        elif name == 'Maruti Wagon R LXI Minor':
            name_enc = 940
        elif name == 'Maruti Wagon R Stingray LXI':
            name_enc = 941
        elif name == 'Maruti Wagon R Stingray VXI':
            name_enc = 942
        elif name == 'Maruti Wagon R VX':
            name_enc = 943
        elif name == 'Maruti Wagon R VXI':
            name_enc = 944
        elif name == 'Maruti Wagon R VXI AMT':
            name_enc = 945
        elif name == 'Maruti Wagon R VXI AMT1.2BSIV':
            name_enc = 946
        elif name == 'Maruti Wagon R VXI BS IV':
            name_enc = 947
        elif name == 'Maruti Wagon R VXI BS IV with ABS':
            name_enc = 948
        elif name == 'Maruti Wagon R VXI BSII':
            name_enc = 949
        elif name == 'Maruti Wagon R VXI BSIII':
            name_enc = 950
        elif name == 'Maruti Wagon R VXI Minor':
            name_enc = 951
        elif name == 'Maruti Wagon R VXI Minor ABS':
            name_enc = 952
        elif name == 'Maruti Wagon R VXI Optional':
            name_enc = 953
        elif name == 'Maruti Wagon R VXI Plus Optional':
            name_enc = 954
        elif name == 'Maruti Wagon R VXi BSII':
            name_enc = 955
        elif name == 'Maruti Wagon R ZXI 1.2':
            name_enc = 956
        elif name == 'Maruti Zen D':
            name_enc = 957
        elif name == 'Maruti Zen D PS':
            name_enc = 958
        elif name == 'Maruti Zen Estilo 1.1 LXI BSIII':
            name_enc = 959
        elif name == 'Maruti Zen Estilo 1.1 VXI BSIII':
            name_enc = 960
        elif name == 'Maruti Zen Estilo LX BSIII':
            name_enc = 961
        elif name == 'Maruti Zen Estilo LX BSIV':
            name_enc = 962
        elif name == 'Maruti Zen Estilo LXI BS IV':
            name_enc = 963
        elif name == 'Maruti Zen Estilo LXI BSIII':
            name_enc = 964
        elif name == 'Maruti Zen Estilo LXI Green (CNG)':
            name_enc = 965
        elif name == 'Maruti Zen Estilo Sports':
            name_enc = 966
        elif name == 'Maruti Zen Estilo VXI BSIII':
            name_enc = 967
        elif name == 'Maruti Zen Estilo VXI BSIV':
            name_enc = 968
        elif name == 'Maruti Zen LX':
            name_enc = 969
        elif name == 'Maruti Zen LX - BS III':
            name_enc = 970
        elif name == 'Maruti Zen LXI':
            name_enc = 971
        elif name == 'Maruti Zen LXi - BS III':
            name_enc = 972
        elif name == 'Maruti Zen LXi BSII':
            name_enc = 973
        elif name == 'Maruti Zen VX':
            name_enc = 974
        elif name == 'Maruti Zen VXI':
            name_enc = 975
        elif name == 'Maruti Zen VXi - BS III':
            name_enc = 976
        
    elif brand == 'Renault':
        brand_enc = 23
        if name == 'Renault Captur 1.5 Diesel RXT':
            name_enc = 977
        elif name == 'Renault Captur 1.5 Diesel RXT Mono':
            name_enc = 978
        elif name == 'Renault Duster 110PS Diesel RxL':
            name_enc = 979
        elif name == 'Renault Duster 110PS Diesel RxZ':
            name_enc = 980
        elif name == 'Renault Duster 110PS Diesel RxZ AWD':
            name_enc = 981
        elif name == 'Renault Duster 110PS Diesel RxZ Plus':
            name_enc = 982
        elif name == 'Renault Duster 85PS Diesel RxE':
            name_enc = 983
        elif name == 'Renault Duster 85PS Diesel RxL':
            name_enc = 984
        elif name == 'Renault Duster 85PS Diesel RxL Optional':
            name_enc = 985
        elif name == 'Renault Duster 85PS Diesel RxL Plus':
            name_enc = 986
        elif name == 'Renault Duster 85PS Diesel RxZ':
            name_enc = 987
        elif name == 'Renault Duster Petrol RxL':
            name_enc = 988
        elif name == 'Renault Duster RXL AWD':
            name_enc = 989
        elif name == 'Renault Fluence 1.5':
            name_enc = 990
        elif name == 'Renault KWID 1.0':
            name_enc = 991
        elif name == 'Renault KWID 1.0 RXL':
            name_enc = 992
        elif name == 'Renault KWID 1.0 RXT Optional':
            name_enc = 993
        elif name == 'Renault KWID AMT':
            name_enc = 994
        elif name == 'Renault KWID Climber 1.0 AMT':
            name_enc = 995
        elif name == 'Renault KWID Climber 1.0 AMT BSIV':
            name_enc = 996
        elif name == 'Renault KWID Climber 1.0 MT Opt BSIV':
            name_enc = 997
        elif name == 'Renault KWID RXE':
            name_enc = 998
        elif name == 'Renault KWID RXL':
            name_enc = 999
        elif name == 'Renault KWID RXL BSIV':
            name_enc = 1000
        elif name == 'Renault KWID RXT':
            name_enc = 1001
        elif name == 'Renault KWID RXT BSIV':
            name_enc = 1002
        elif name == 'Renault KWID RXT Optional':
            name_enc = 1003
        elif name == 'Renault Koleos 2.0 Diesel':
            name_enc = 1004
        elif name == 'Renault Lodgy 85PS RxL':
            name_enc = 1005
        elif name == 'Renault Lodgy Stepway 85PS RXZ 8S':
            name_enc = 1006
        elif name == 'Renault Pulse RxL':
            name_enc = 1007
        elif name == 'Renault Pulse RxZ':
            name_enc = 1008
        elif name == 'Renault Pulse RxZ Optional':
            name_enc = 1009
        elif name == 'Renault Scala Diesel RxL':
            name_enc = 1010
        elif name == 'Renault Scala RxL':
            name_enc = 1011
        elif name == 'Renault Triber RXT BSIV':
            name_enc = 1012

    elif brand == 'Tata':
        brand_enc = 25
        if name == 'Tata Altroz XE':
            name_enc = 1013
        elif name == 'Tata Altroz XZ':
            name_enc = 1014
        elif name == 'Tata Aria Pleasure 4x2':
            name_enc = 1015
        elif name == 'Tata Aria Pure LX 4x2':
            name_enc = 1016
        elif name == 'Tata Bolt Quadrajet XE':
            name_enc = 1017
        elif name == 'Tata Bolt Revotron XE':
            name_enc = 1018
        elif name == 'Tata Bolt Revotron XM':
            name_enc = 1019
        elif name == 'Tata Harrier XE':
            name_enc = 1020
        elif name == 'Tata Harrier XZ BSIV':
            name_enc = 1021
        elif name == 'Tata Hexa XM':
            name_enc = 1022
        elif name == 'Tata Hexa XT':
            name_enc = 1023
        elif name == 'Tata Hexa XT 4X4':
            name_enc = 1024
        elif name == 'Tata Hexa XTA':
            name_enc = 1025
        elif name == 'Tata Indica DL':
            name_enc = 1026
        elif name == 'Tata Indica DLE':
            name_enc = 1027
        elif name == 'Tata Indica DLS':
            name_enc = 1028
        elif name == 'Tata Indica DLX':
            name_enc = 1029
        elif name == 'Tata Indica GLS BS IV':
            name_enc = 1030
        elif name == 'Tata Indica LSI':
            name_enc = 1031
        elif name == 'Tata Indica LXI':
            name_enc = 1032
        elif name == 'Tata Indica V2 2001-2011 DLS BSIII':
            name_enc = 1033
        elif name == 'Tata Indica V2 DLS BSII':
            name_enc = 1034
        elif name == 'Tata Indica Vista Aqua 1.2 Safire BSIV':
            name_enc = 1035
        elif name == 'Tata Indica Vista Aqua 1.3 Quadrajet':
            name_enc = 1036
        elif name == 'Tata Indica Vista Aqua 1.3 Quadrajet ABS BSIV':
            name_enc = 1037
        elif name == 'Tata Indica Vista Aqua 1.3 Quadrajet BSIV':
            name_enc = 1038
        elif name == 'Tata Indica Vista Aqua 1.4 TDI':
            name_enc = 1039
        elif name == 'Tata Indica Vista Aqua TDI BSIII':
            name_enc = 1040
        elif name == 'Tata Indica Vista Aura 1.2 Safire':
            name_enc = 1041
        elif name == 'Tata Indica Vista Aura 1.3 Quadrajet':
            name_enc = 1042
        elif name == 'Tata Indica Vista Aura 1.3 Quadrajet BSIV':
            name_enc = 1043
        elif name == 'Tata Indica Vista Aura Plus 1.3 Quadrajet':
            name_enc = 1044
        elif name == 'Tata Indica Vista Quadrajet 90 VX':
            name_enc = 1045
        elif name == 'Tata Indica Vista Quadrajet LS':
            name_enc = 1046
        elif name == 'Tata Indica Vista Quadrajet LX':
            name_enc = 1047
        elif name == 'Tata Indica Vista Quadrajet VX':
            name_enc = 1048
        elif name == 'Tata Indica Vista TDI LS':
            name_enc = 1049
        elif name == 'Tata Indica Vista TDI LX':
            name_enc = 1050
        elif name == 'Tata Indica Vista Terra 1.4 TDI':
            name_enc = 1051
        elif name == 'Tata Indica Vista Terra Quadrajet 1.3L':
            name_enc = 1052
        elif name == 'Tata Indica Vista Terra Quadrajet 1.3L BS IV':
            name_enc = 1053
        elif name == 'Tata Indica Vista Terra TDI BSIII':
            name_enc = 1054
        elif name == 'Tata Indigo CR4':
            name_enc = 1055
        elif name == 'Tata Indigo CS Emax CNG GLX':
            name_enc = 1056
        elif name == 'Tata Indigo CS LE (TDI) BS-III':
            name_enc = 1057
        elif name == 'Tata Indigo CS LS (TDI) BS-III':
            name_enc = 1058
        elif name == 'Tata Indigo CS LX (TDI) BS-III':
            name_enc = 1059
        elif name == 'Tata Indigo CS eLS BS IV':
            name_enc = 1060
        elif name == 'Tata Indigo CS eLX BS IV':
            name_enc = 1061
        elif name == 'Tata Indigo Classic Dicor':
            name_enc = 1062
        elif name == 'Tata Indigo GLE BSIII':
            name_enc = 1063
        elif name == 'Tata Indigo GLS':
            name_enc = 1064
        elif name == 'Tata Indigo GLX':
            name_enc = 1065
        elif name == 'Tata Indigo Grand Dicor':
            name_enc = 1066
        elif name == 'Tata Indigo Grand Petrol':
            name_enc = 1067
        elif name == 'Tata Indigo LS':
            name_enc = 1068
        elif name == 'Tata Indigo LS BSII':
            name_enc = 1069
        elif name == 'Tata Indigo LS Dicor':
            name_enc = 1070
        elif name == 'Tata Indigo LX':
            name_enc = 1071
        elif name == 'Tata Indigo LX Dicor':
            name_enc = 1072
        elif name == 'Tata Indigo TDI':
            name_enc = 1073
        elif name == 'Tata Manza Aqua Quadrajet BS IV':
            name_enc = 1074
        elif name == 'Tata Manza Aura (ABS) Quadrajet BS IV':
            name_enc = 1075
        elif name == 'Tata Manza Aura (ABS) Safire BS IV':
            name_enc = 1076
        elif name == 'Tata Manza Aura Quadrajet':
            name_enc = 1077
        elif name == 'Tata Manza Aura Quadrajet BS IV':
            name_enc = 1078
        elif name == 'Tata Manza Aura Safire':
            name_enc = 1079
        elif name == 'Tata Manza Aura Safire BS IV':
            name_enc = 1080
        elif name == 'Tata Manza Club Class Quadrajet90 EX':
            name_enc = 1081
        elif name == 'Tata Manza Club Class Quadrajet90 LS':
            name_enc = 1082
        elif name == 'Tata Manza Club Class Quadrajet90 LX':
            name_enc = 1083
        elif name == 'Tata Manza Club Class Quadrajet90 VX':
            name_enc = 1084
        elif name == 'Tata Manza ELAN Quadrajet BS IV':
            name_enc = 1085
        elif name == 'Tata Nano CX':
            name_enc = 1086
        elif name == 'Tata Nano CX SE':
            name_enc = 1087
        elif name == 'Tata Nano Cx BSIII':
            name_enc = 1088
        elif name == 'Tata Nano Cx BSIV':
            name_enc = 1089
        elif name == 'Tata Nano LX':
            name_enc = 1090
        elif name == 'Tata Nano LX SE':
            name_enc = 1091
        elif name == 'Tata Nano Lx':
            name_enc = 1092
        elif name == 'Tata Nano Lx BSIII':
            name_enc = 1093
        elif name == 'Tata Nano Lx BSIV':
            name_enc = 1094
        elif name == 'Tata Nano STD':
            name_enc = 1095
        elif name == 'Tata Nano Std':
            name_enc = 1096
        elif name == 'Tata Nano Std BSII':
            name_enc = 1097
        elif name == 'Tata Nano Twist XE':
            name_enc = 1098
        elif name == 'Tata Nano Twist XT':
            name_enc = 1099
        elif name == 'Tata Nano XM':
            name_enc = 1100
        elif name == 'Tata New Safari 3L Dicor LX 4x2':
            name_enc = 1101
        elif name == 'Tata New Safari 4X2':
            name_enc = 1102
        elif name == 'Tata New Safari 4X4':
            name_enc = 1103
        elif name == 'Tata New Safari 4X4 EX':
            name_enc = 1104
        elif name == 'Tata New Safari DICOR 2.2 EX 4x2':
            name_enc = 1105
        elif name == 'Tata New Safari DICOR 2.2 EX 4x4':
            name_enc = 1106
        elif name == 'Tata New Safari DICOR 2.2 GX 4x2':
            name_enc = 1107
        elif name == 'Tata New Safari DICOR 2.2 GX 4x2 BS IV':
            name_enc = 1108
        elif name == 'Tata New Safari DICOR 2.2 VX 4x2':
            name_enc = 1109
        elif name == 'Tata New Safari DICOR 2.2 VX 4x4':
            name_enc = 1110
        elif name == 'Tata New Safari Dicor EX 4X2 BS IV':
            name_enc = 1111
        elif name == 'Tata Nexon 1.2 Revotron XM':
            name_enc = 1112
        elif name == 'Tata Nexon 1.2 Revotron XZ Plus':
            name_enc = 1113
        elif name == 'Tata Nexon 1.2 Revotron XZ Plus Dual Tone':
            name_enc = 1114
        elif name == 'Tata Nexon 1.5 Revotorq XM':
            name_enc = 1115
        elif name == 'Tata Nexon 1.5 Revotorq XZ':
            name_enc = 1116
        elif name == 'Tata Safari DICOR 2.2 EX 4x2':
            name_enc = 1117
        elif name == 'Tata Safari Storme EX':
            name_enc = 1118
        elif name == 'Tata Safari Storme VX':
            name_enc = 1119
        elif name == 'Tata Safari Storme VX Varicor 400':
            name_enc = 1120
        elif name == 'Tata Spacio SA 6 Seater':
            name_enc = 1121
        elif name == 'Tata Sumo GX TC 7 Str BSIII':
            name_enc = 1122
        elif name == 'Tata Sumo GX TC 8 Str':
            name_enc = 1123
        elif name == 'Tata Sumo Gold EX':
            name_enc = 1124
        elif name == 'Tata Sumo Gold EX BSIII':
            name_enc = 1125
        elif name == 'Tata Sumo LX':
            name_enc = 1126
        elif name == 'Tata Sumo SE Plus BSIII':
            name_enc = 1127
        elif name == 'Tata Sumo Victa CX 7/9 Str BSII':
            name_enc = 1128
        elif name == 'Tata Sumo Victa EX 7/9 Str BSII':
            name_enc = 1129
        elif name == 'Tata Tiago 1.05 Revotorq XE':
            name_enc = 1130
        elif name == 'Tata Tiago 1.05 Revotorq XM':
            name_enc = 1131
        elif name == 'Tata Tiago 1.05 Revotorq XT Option':
            name_enc = 1132
        elif name == 'Tata Tiago 1.05 Revotorq XZ Plus':
            name_enc = 1133
        elif name == 'Tata Tiago 1.2 Revotron XE':
            name_enc = 1134
        elif name == 'Tata Tiago 1.2 Revotron XT':
            name_enc = 1135
        elif name == 'Tata Tiago 1.2 Revotron XTA':
            name_enc = 1136
        elif name == 'Tata Tiago 1.2 Revotron XZ':
            name_enc = 1137
        elif name == 'Tata Tiago 1.2 Revotron XZA':
            name_enc = 1138
        elif name == 'Tata Tiago 2019-2020 XE Diesel':
            name_enc = 1139
        elif name == 'Tata Tiago 2019-2020 XZ':
            name_enc = 1140
        elif name == 'Tata Tiago NRG Petrol':
            name_enc = 1141
        elif name == 'Tata Tiago XT':
            name_enc = 1142
        elif name == 'Tata Tiago XZA AMT':
            name_enc = 1143
        elif name == 'Tata Tigor 1.2 Revotron XM':
            name_enc = 1144
        elif name == 'Tata Tigor 1.2 Revotron XT':
            name_enc = 1145
        elif name == 'Tata Tigor 1.2 Revotron XZ Option':
            name_enc = 1146
        elif name == 'Tata Venture EX':
            name_enc = 1147
        elif name == 'Tata Winger Deluxe - Hi Roof (AC)':
            name_enc = 1148
        elif name == 'Tata Xenon XT EX 4X2':
            name_enc = 1149
        elif name == 'Tata Xenon XT EX 4X4':
            name_enc = 1150
        elif name == 'Tata Zest Quadrajet 1.3':
            name_enc = 1151
        elif name == 'Tata Zest Quadrajet 1.3 75PS XE':
            name_enc = 1152
        elif name == 'Tata Zest Quadrajet 1.3 XM':
            name_enc = 1153
        elif name == 'Tata Zest Revotron 1.2 XT':
            name_enc = 1154
        elif name == 'Tata Zest Revotron 1.2T XE':
            name_enc = 1155
        elif name == 'Tata Zest Revotron 1.2T XMS':
            name_enc = 1156
        
    elif brand == 'Toyota':
        brand_enc = 26
        if name == 'Toyota Camry 2.5 Hybrid':
            name_enc = 1157
        elif name == 'Toyota Camry Hybrid 2.5':
            name_enc = 1158
        elif name == 'Toyota Camry M/t':
            name_enc = 1159
        elif name == 'Toyota Corolla AE':
            name_enc = 1160
        elif name == 'Toyota Corolla Altis 1.8 GL':
            name_enc = 1161
        elif name == 'Toyota Corolla Altis 1.8 J':
            name_enc = 1162
        elif name == 'Toyota Corolla Altis 1.8 VL AT':
            name_enc = 1163
        elif name == 'Toyota Corolla Altis 1.8 VL CVT':
            name_enc = 1164
        elif name == 'Toyota Corolla Altis D-4D J':
            name_enc = 1165
        elif name == 'Toyota Corolla Altis Diesel D4DG':
            name_enc = 1166
        elif name == 'Toyota Corolla Altis Diesel D4DGL':
            name_enc = 1167
        elif name == 'Toyota Corolla Altis Diesel D4DJ':
            name_enc = 1168
        elif name == 'Toyota Corolla Altis G':
            name_enc = 1169
        elif name == 'Toyota Corolla Altis G AT':
            name_enc = 1170
        elif name == 'Toyota Corolla Altis GL MT':
            name_enc = 1171
        elif name == 'Toyota Corolla Executive (HE)':
            name_enc = 1172
        elif name == 'Toyota Corolla H2':
            name_enc = 1173
        elif name == 'Toyota Corolla H3':
            name_enc = 1174
        elif name == 'Toyota Corolla H6':
            name_enc = 1175
        elif name == 'Toyota Etios 1.4 VXD':
            name_enc = 1176
        elif name == 'Toyota Etios 1.5 V':
            name_enc = 1177
        elif name == 'Toyota Etios Cross 1.2L G':
            name_enc = 1178
        elif name == 'Toyota Etios Cross 1.4L GD':
            name_enc = 1179
        elif name == 'Toyota Etios GD':
            name_enc = 1180
        elif name == 'Toyota Etios GD SP':
            name_enc = 1181
        elif name == 'Toyota Etios Liva 1.2 G':
            name_enc = 1182
        elif name == 'Toyota Etios Liva 1.2 V':
            name_enc = 1183
        elif name == 'Toyota Etios Liva 1.2 VX':
            name_enc = 1184
        elif name == 'Toyota Etios Liva 1.4 VD':
            name_enc = 1185
        elif name == 'Toyota Etios Liva G':
            name_enc = 1186
        elif name == 'Toyota Etios Liva GD':
            name_enc = 1187
        elif name == 'Toyota Etios Liva GD SP':
            name_enc = 1188
        elif name == 'Toyota Etios Liva VD':
            name_enc = 1189
        elif name == 'Toyota Etios Liva VX':
            name_enc = 1190
        elif name == 'Toyota Etios V':
            name_enc = 1191
        elif name == 'Toyota Etios VD':
            name_enc = 1192
        elif name == 'Toyota Etios VX':
            name_enc = 1193
        elif name == 'Toyota Etios VXD':
            name_enc = 1194
        elif name == 'Toyota Fortuner 2.7 2WD AT':
            name_enc = 1195
        elif name == 'Toyota Fortuner 2.8 2WD AT BSIV':
            name_enc = 1196
        elif name == 'Toyota Fortuner 2.8 4WD AT BSIV':
            name_enc = 1197
        elif name == 'Toyota Fortuner 3.0 Diesel':
            name_enc = 1198
        elif name == 'Toyota Fortuner 4x2 AT':
            name_enc = 1199
        elif name == 'Toyota Fortuner 4x2 Manual':
            name_enc = 1200
        elif name == 'Toyota Fortuner 4x4 MT':
            name_enc = 1201
        elif name == 'Toyota Innova 2.0 GX 8 STR BSIV':
            name_enc = 1202
        elif name == 'Toyota Innova 2.0 VX 7 Seater':
            name_enc = 1203
        elif name == 'Toyota Innova 2.5 E 8 STR':
            name_enc = 1204
        elif name == 'Toyota Innova 2.5 E Diesel MS 7-seater':
            name_enc = 1205
        elif name == 'Toyota Innova 2.5 EV Diesel MS 7 Str BSIII':
            name_enc = 1206
        elif name == 'Toyota Innova 2.5 EV Diesel PS 7 Seater BSIII':
            name_enc = 1207
        elif name == 'Toyota Innova 2.5 G (Diesel) 7 Seater':
            name_enc = 1208
        elif name == 'Toyota Innova 2.5 G (Diesel) 7 Seater BS IV':
            name_enc = 1209
        elif name == 'Toyota Innova 2.5 G (Diesel) 8 Seater':
            name_enc = 1210
        elif name == 'Toyota Innova 2.5 G (Diesel) 8 Seater BS IV':
            name_enc = 1211
        elif name == 'Toyota Innova 2.5 G1 BSIV':
            name_enc = 1212
        elif name == 'Toyota Innova 2.5 G3':
            name_enc = 1213
        elif name == 'Toyota Innova 2.5 G4 Diesel 7-seater':
            name_enc = 1214
        elif name == 'Toyota Innova 2.5 G4 Diesel 8-seater':
            name_enc = 1215
        elif name == 'Toyota Innova 2.5 GX (Diesel) 7 Seater':
            name_enc = 1216
        elif name == 'Toyota Innova 2.5 GX (Diesel) 7 Seater BS IV':
            name_enc = 1217
        elif name == 'Toyota Innova 2.5 GX (Diesel) 8 Seater':
            name_enc = 1218
        elif name == 'Toyota Innova 2.5 GX (Diesel) 8 Seater BS IV':
            name_enc = 1219
        elif name == 'Toyota Innova 2.5 GX 7 STR':
            name_enc = 1220
        elif name == 'Toyota Innova 2.5 GX 7 STR BSIV':
            name_enc = 1221
        elif name == 'Toyota Innova 2.5 GX 8 STR BSIV':
            name_enc = 1222
        elif name == 'Toyota Innova 2.5 V Diesel 7-seater':
            name_enc = 1223
        elif name == 'Toyota Innova 2.5 V Diesel 8-seater':
            name_enc = 1224
        elif name == 'Toyota Innova 2.5 VX (Diesel) 7 Seater':
            name_enc = 1225
        elif name == 'Toyota Innova 2.5 VX (Diesel) 7 Seater BS IV':
            name_enc = 1226
        elif name == 'Toyota Innova 2.5 VX (Diesel) 8 Seater':
            name_enc = 1227
        elif name == 'Toyota Innova 2.5 VX (Diesel) 8 Seater BS IV':
            name_enc = 1228
        elif name == 'Toyota Innova 2.5 VX 8 STR':
            name_enc = 1229
        elif name == 'Toyota Innova 2.5 VX 8 STR BSIV':
            name_enc = 1230
        elif name == 'Toyota Innova 2.5 Z Diesel 7 Seater BS IV':
            name_enc = 1231
        elif name == 'Toyota Innova Crysta 2.4 G MT BSIV':
            name_enc = 1232
        elif name == 'Toyota Innova Crysta 2.4 GX AT':
            name_enc = 1233
        elif name == 'Toyota Innova Crysta 2.4 GX MT 8S BSIV':
            name_enc = 1234
        elif name == 'Toyota Innova Crysta 2.4 VX MT':
            name_enc = 1235
        elif name == 'Toyota Innova Crysta 2.4 VX MT 8S BSIV':
            name_enc = 1236
        elif name == 'Toyota Innova Crysta 2.4 VX MT BSIV':
            name_enc = 1237
        elif name == 'Toyota Innova Crysta 2.4 ZX MT':
            name_enc = 1238
        elif name == 'Toyota Innova Crysta 2.5 VX BS IV':
            name_enc = 1239
        elif name == 'Toyota Innova Crysta 2.8 GX AT BSIV':
            name_enc = 1240
        elif name == 'Toyota Innova Crysta 2.8 ZX AT BSIV':
            name_enc = 1241
        elif name == 'Toyota Qualis FS B3':
            name_enc = 1242
        elif name == 'Toyota Yaris G':
            name_enc = 1243

    elif brand == 'Volkswagen':
        brand_enc = 27
        if name == 'Volkswagen Ameo 1.2 MPI Trendline':
            name_enc = 1244
        elif name == 'Volkswagen Ameo 1.5 TDI Comfortline':
            name_enc = 1245
        elif name == 'Volkswagen Ameo 1.5 TDI Highline':
            name_enc = 1246
        elif name == 'Volkswagen Ameo 1.5 TDI Highline 16 Alloy':
            name_enc = 1247
        elif name == 'Volkswagen Ameo 1.5 TDI Highline Plus 16': 
            name_enc = 1248
        elif name == 'Volkswagen CrossPolo 1.2 MPI':
            name_enc = 1249
        elif name == 'Volkswagen Jetta 1.4 TSI Comfortline':
            name_enc = 1250
        elif name == 'Volkswagen Jetta 1.9 Highline TDI':
            name_enc = 1251
        elif name == 'Volkswagen Jetta 1.9 L TDI':
            name_enc = 1252
        elif name == 'Volkswagen Jetta 1.9 TDI Comfortline DSG':
            name_enc = 1253
        elif name == 'Volkswagen Jetta 1.9 TDI Trendline':
            name_enc = 1254
        elif name == 'Volkswagen Jetta 2.0 TDI Comfortline':
            name_enc = 1255
        elif name == 'Volkswagen Jetta 2.0 TDI Trendline':
            name_enc = 1256
        elif name == 'Volkswagen Jetta 2.0L TDI Comfortline':
            name_enc = 1257
        elif name == 'Volkswagen Jetta 2.0L TDI Highline': 
            name_enc = 1258
        elif name == 'Volkswagen Jetta 2.0L TDI Highline AT':
            name_enc = 1259
        elif name == 'Volkswagen Passat 1.8 TSI MT':
            name_enc = 1260
        elif name == 'Volkswagen Polo 1.0 MPI Trendline':
            name_enc = 1261
        elif name == 'Volkswagen Polo 1.0 TSI Highline Plus': 
            name_enc = 1262
        elif name == 'Volkswagen Polo 1.2 MPI Comfortline':
            name_enc = 1263
        elif name == 'Volkswagen Polo 1.2 MPI Highline':
            name_enc = 1264
        elif name == 'Volkswagen Polo 1.5 TDI Comfortline':
            name_enc = 1265
        elif name == 'Volkswagen Polo 1.5 TDI Highline':
            name_enc = 1266
        elif name == 'Volkswagen Polo 1.5 TDI Trendline':
            name_enc = 1267
        elif name == 'Volkswagen Polo 2015-2019 1.2 MPI Highline':
            name_enc = 1268
        elif name == 'Volkswagen Polo Diesel Comfortline 1.2L':
            name_enc = 1269
        elif name == 'Volkswagen Polo Diesel Highline 1.2L':
            name_enc = 1270
        elif name == 'Volkswagen Polo Diesel Trendline 1.2L':
            name_enc = 1271
        elif name == 'Volkswagen Polo GT 1.0 TSI': 
            name_enc = 1272
        elif name == 'Volkswagen Polo GTI': 
            name_enc = 1273
        elif name == 'Volkswagen Polo Petrol Comfortline 1.2L':
            name_enc = 1274
        elif name == 'Volkswagen Polo Petrol Highline 1.2L':
            name_enc = 1275
        elif name == 'Volkswagen Polo SR Petrol 1.2L':
            name_enc = 1276
        elif name == 'Volkswagen Vento 1.0 TSI Highline Plus':
            name_enc = 1277
        elif name == 'Volkswagen Vento 1.5 Highline Plus AT 16 Alloy':
            name_enc = 1278
        elif name == 'Volkswagen Vento 1.5 TDI Comfortline':
            name_enc = 1279
        elif name == 'Volkswagen Vento 1.5 TDI Comfortline AT':
            name_enc = 1280
        elif name == 'Volkswagen Vento 1.5 TDI Highline':
            name_enc = 1281
        elif name == 'Volkswagen Vento 1.5 TDI Highline AT':
            name_enc = 1282
        elif name == 'Volkswagen Vento 1.5 TDI Highline BSIV':
            name_enc = 1283
        elif name == 'Volkswagen Vento 1.5 TDI Highline Plus AT':
            name_enc = 1284
        elif name == 'Volkswagen Vento 1.5 TDI Highline Plus AT BSIV':
            name_enc = 1285
        elif name == 'Volkswagen Vento 1.6 Highline':
            name_enc = 1286
        elif name == 'Volkswagen Vento Celeste 1.5 TDI Highline AT':
            name_enc = 1287
        elif name == 'Volkswagen Vento Diesel Comfortline':
            name_enc = 1288
        elif name == 'Volkswagen Vento Diesel Highline':
            name_enc = 1289
        elif name == 'Volkswagen Vento Diesel Style Limited Edition':
            name_enc = 1290
        elif name == 'Volkswagen Vento Diesel Trendline':
            name_enc = 1291
        elif name == 'Volkswagen Vento IPL II Diesel Trendline':
            name_enc = 1292
        elif name == 'Volkswagen Vento Magnific 1.6 Highline':
            name_enc = 1293
        elif name == 'Volkswagen Vento New Diesel Highline':
            name_enc = 1294
        elif name == 'Volkswagen Vento Petrol Highline':
            name_enc = 1295
        elif name == 'Volkswagen Vento Petrol Highline AT':
            name_enc = 1296

# fuel_enc
    if fuel == 'CNG':
        fuel_enc = 0
    elif fuel == 'Diesel':
        fuel_enc = 1
    elif fuel == 'LPG':
        fuel_enc = 2
    elif fuel == 'Petrol':
        fuel_enc = 3
  
# owner_enc
# 'First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'
    if owner == 'First Owner':
        owner_enc = 0
    elif owner == 'Fourth & Above Owner':
        owner_enc = 1
    elif owner == 'Second Owner':
        owner_enc = 2
    elif owner == 'Test Drive Car':
        owner_enc = 3
    elif owner == 'Third Owner':
        owner_enc = 4


# seller_type_Dealer	seller_type_Individual	seller_type_Trustmark Dealer
# Seller type
    if seller_type == 'Dealer':
        seller_type_Dealer = 1
        seller_type_Individual = 0 
        seller_type_Trustmark_Dealer = 0
    elif seller_type == 'Individual':
        seller_type_Dealer = 0 
        seller_type_Individual = 1 
        seller_type_Trustmark_Dealer = 0
    elif seller_type == 'Trustmark Dealer':
        seller_type_Dealer = 0
        seller_type_Individual = 0 
        seller_type_Trustmark_Dealer = 1


# transmission
# transmission_Automatic	transmission_Manual
    if transmission == 'Automatic':
        transmission_Automatic, transmission_Manual = 1,0
    elif transmission == 'Manual':
        transmission_Automatic, transmission_Manual = 0,1

    test = np.array([year, km_driven, name_enc, brand_enc, fuel_enc, owner_enc, seller_type_Dealer, seller_type_Individual, seller_type_Trustmark_Dealer, transmission_Automatic, transmission_Manual]) 
    test = test.reshape(1,11)
    st.success(Model.predict(test)[0])





# brand  name  year  fuel seller_type transmission owner km_driven
