
from mailmerge import MailMerge
from datetime import date
from tkinter import *
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
from tkinter import ttk 
import tkinter as tk
import os
import sys
import time
from datetime import date
import shutil

print('The printed out letter will appear here.')
print('========================================')
print('''In the event that for some reason the letter doesn't save to a file it can be copied and pasted from here manually.''')
print('========================================')
root = tk.Tk()

template = r'C:\Users\Henry Pope IV\Documents\Follow-up Service\Programs\Ascent-Dental-Letter-Template.docx'

document = MailMerge(template)

root.title('')
root.geometry('+50+50')
root.iconbitmap('')

OFFICES = [
    'No Input',
    '250 N Main St',
    '66 Dwight Rd',
    '294 N Main St'
]

OfficeVar = tk.StringVar()
OfficeVar.set(OFFICES[0])

Title = Label(text='Email Follow-up Automator')
Title.pack()


BlankSpacer1 = Label(text='')
BlankSpacer1.pack()

NameLabel = Label(text='Patient Name')
NameLabel.pack()

Name = Entry(root)
Name.pack()

OfficeLabel = Label(text='Which office did the patient visit?')
OfficeLabel.pack()

OfficeDropdown = OptionMenu(root, OfficeVar, *OFFICES)
OfficeDropdown.pack()

DateOfVisitLabel = Label(text='When was the patients last visit?')
DateOfVisitLabel.pack()

DateOfVisit = DateEntry(root)
DateOfVisit.pack()

NextVisitLabel = Label(text='When is the patients next visit?')
NextVisitLabel.pack()

NextVisit = DateEntry(root)
NextVisit.pack()

BlankSpacer2 = Label(text='')
BlankSpacer2.pack()

TypeOfTreatment = Label(text='What type of treatment does this patient require?')
TypeOfTreatment.pack()

RestorativeTreatmentVar  = IntVar(root)
WaitAndWatchVar = IntVar(root)
CrownTreatmentVar = IntVar(root)
RootCanalTreatmentVar = IntVar(root)
WisdomTeethVar = IntVar(root)
WaitAndWatchOnWisdomTeethVar = IntVar(root)
ExtractingTreatmentVar = IntVar(root)

BlankSpacer3 = Label(text='')
BlankSpacer3.pack()

###########################

top = Toplevel()
top.geometry('+350+50')
top.title('Patient Options')

RestorativeTreatmentNumVar = StringVar()

BlankSpacer8 = Label(text='')
BlankSpacer8.pack()

PatientSettings = Label(top, text='Patient Options')
PatientSettings.pack()

WaitAndWatch = Checkbutton(top, text='Wait and Watch', variable=WaitAndWatchVar)
WaitAndWatch.pack()

WaitAndWatchToothLabel = Label(top, text='Tooth #?') 
WaitAndWatchToothLabel.pack()

WaitAndWatchToothNumber = Spinbox(top, from_=0, to=32, width=4)
WaitAndWatchToothNumber.pack()

BlankSpacer7 = Label(top, text='')
BlankSpacer7.pack()

spacer1 = Label(top, text='====')
spacer1.pack()

RestorativeTreatment = Checkbutton(top,  text='Restorative Treatment', variable=RestorativeTreatmentVar)
RestorativeTreatment.pack()

RestorativeTreatmentLabel = Label(top, text='Tooth #?')
RestorativeTreatmentLabel.pack()

RestorativeTreatmentToothNumber = Spinbox(top, from_=0, to=32, width=4)
RestorativeTreatmentToothNumber.pack()

spacer2 = Label(top, text='====')
spacer2.pack()


CrownTreatment = Checkbutton(top, text='Crown Treatment', variable=CrownTreatmentVar)
CrownTreatment.pack()

CrownTreatmentLabel = Label(top, text='Tooth #?')
CrownTreatmentLabel.pack()

spacer3 = Label(top, text='====')
spacer3.pack()

CrownTreatmentNumber = Spinbox(top, from_=0, to=32, width=4)
CrownTreatmentNumber.pack()

spacer6 = Label(top, text='====')
spacer6.pack()

RootCanalTreatment = Checkbutton(top,  text='Root Canal Treatment', variable=RootCanalTreatmentVar)
RootCanalTreatment.pack()

spacer8 = Label(top, text='====')
spacer8.pack()

RootCanalTreatmentNumber = Spinbox(top, from_=0, to=32, width=4)
RootCanalTreatmentNumber.pack()

spacer5 = Label(top, text='====')
spacer5.pack()

WisdomTeeth = Checkbutton(top,  text='Wisdom Teeth', variable=WisdomTeethVar)
WisdomTeeth.pack()

spacer5 = Label(top, text='====')
spacer5.pack()

WisdomTeethNumber = Spinbox(top, from_=0, to=32, width=4)
WisdomTeethNumber.pack()

spacer11 = Label(top, text='====')
spacer11.pack()

WaitAndWatchOnWisdomTeeth = Checkbutton(top,  text='Wait and Watch on Wisdom Teeth', variable=WaitAndWatchOnWisdomTeethVar)
WaitAndWatchOnWisdomTeeth.pack()

spacer7 = Label(top, text='====')
spacer7.pack()

WaitAndWatchOnWisdomTeethNumber = Spinbox(top, from_=0, to=32, width=4)
WaitAndWatchOnWisdomTeethNumber.pack()

spacer10 = Label(top, text='====')
spacer10.pack()

ExtractingTreatment = Checkbutton(top,  text='Extraction Treatment', variable=ExtractingTreatmentVar)
ExtractingTreatment.pack()

spacer9 = Label(top, text='====')
spacer9.pack()

ExtractingTreatmentNumber = Spinbox(top, from_=0, to=32, width=4)
ExtractingTreatmentNumber.pack()

BlankSpacer4 = Label(top, text='')
BlankSpacer4.pack()


def submit():

    NameVar = Name.get()

    fileName = NameVar + ' Letter' + '.docx' 

    today = date.today()

    WhichOfficeVar = OfficeVar.get()

    OldVisitVar = DateOfVisit.get()

    NextVisitVar = NextVisit.get()
    

    WaitAndWatchVariable = WaitAndWatchVar.get()

    RestorativeTreatmentVariable = RestorativeTreatmentVar.get()

    CrownTreatmentVariable = CrownTreatmentVar.get()

    RootCanalTreatmentVariable = RootCanalTreatmentVar.get()
 
    WisdomTeethVariable = WisdomTeethVar.get()

    WaitAndWatchOnWisdomTeethVariable = WaitAndWatchOnWisdomTeethVar.get()

    ExtractingTreatmentVariable = ExtractingTreatmentVar.get()


    WaitAndWatchToothNumberPara = WaitAndWatchToothNumber.get()

    RestorativeTreatmentToothNumberPara = RestorativeTreatmentToothNumber.get()

    CrownTreatmentNumberPara = CrownTreatmentNumber.get()

    RootCanalTreatmentNumberPara = RootCanalTreatmentNumber.get()

    WisdomTeethNumberPara = WisdomTeethNumber.get()

    WaitAndWatchOnWisdomTeethNumberPara = WaitAndWatchOnWisdomTeethNumber.get()

    ExtractingTreatmentNumberPara = ExtractingTreatmentNumber.get()
    
    GlobalIntro = '''''' + str(today) + '''
    ''' + NameVar + '''

Dear ''' + NameVar + ''',

It was a pleasure seeing you in our ''' + WhichOfficeVar +  ''' office. Your last dental visit was ''' + OldVisitVar + '''. You presented with chief concern of a cleaning. On today’s visit we took a panoramic, bitewing radiographs and intraoral pictures and performed an exam, a periodontal evaluation, and a dental cleaning.  The reason for the letter is to give a current status of your oral conditions and to provide recommendations to help achieve optimal oral health.  The fees written in this letter are Ascent Dental Care fees.  For further explanation and details regarding your personal treatment pan and out-of-pocket costs, please contact an Office Administrator in our office.

The following chart will hopefully orientate you to the different areas in your mouth.  From back right to back left on the upper jaw, your teeth are numbered 1 – 16.  From back left to back right on the lower jaw, your teeth are numbered 17 – 32.  Your mouth is divided into four quadrants; upper right, upper left, lower left, and lower right.

Upper Right

           Upper Right      |        Upper Left
        1-2-3-4-5-6-7-8     |    9-10-11-12-13-14-15-16
    -----------------------------------------------
            Lower Right     |     Lower Left
    32-31-30-29-28-27-26-25 |    24-23-22-21-20-19-18-17 
    
    
Periodontal Health (6MR)

First, I would recommend that we get you in for a hygiene appointment to clean and polish your teeth and the fee for this is $95 - $260.  Without healthy gums and bone to support your teeth, any dental care that is done can rapidly fail causing additional cost and time.  Our office philosophy is that most periodontal or gum problems can be corrected with either mechanical, chemical or surgical care or a combination of these.  At this time, my recommendation is to place you on a 6 month recall for periodic cleanings and exams.  Also, every 2 – 3 years, I would recommend updating your periodontal readings for future recommendations and the fee would be $115.

Periodontal Health (s/rp)

First, I would recommend that we get you in for a hygiene appointment to clean and polish your teeth and the fee for this is $95 - $260.  Without healthy gums and bone to support your teeth, any dental care that is done can rapidly fail causing additional cost and time.  Our office philosophy is that most periodontal or gum problems can be corrected with either mechanical, chemical or surgical care or a combination of these.  I would recommend that we place you on prescriptions for Perioguard or Therosol, Prevident, and Periostat, which are antibacterial, antibiotic and fluoride treatments.  At this time, I would recommend scaling and root planing by quadrant or full mouth.  The fees for scaling and root planing range from $260- $1040.  Scaling and root planing is recommended when an infection occurs under the gumline and periodontal disease is present. Every 1-2 years, I would recommend updating your periodontal readings for future recommendations and the fee would be $115. 

The fees contained in this letter are estimated fees and are subject to change.  The fees quoted at this time will be honored for a period of 3 months.   Also, please note that sometimes, clinical situations necessitate alterations or modifications in our recommendations.

If these fees and treatment plans are acceptable to you, please sign below.  Signing this letter does not obligate you to do any of the above-mentioned treatment, it simply emphasizes that your options have been explained and our recommendations are understood.  Thank you for choosing Ascent Dental Care for your care.

Once again, it was a pleasure seeing you and if you have any further questions, please do not hesitate to call the office.  We thank you for showing confidence in our office.  Your kind referrals are always appreciated.  Your next visit will be for ''' + NextVisitVar + '''. 

Sincerely,


Kevin Coughlin DMD, MBA, MAGD, LE

Elizabeth Alexander, DMD

Tushin Shah, DDS

    '''

    WaitAndWatchPara = '''
Wait and Watch
    
As far as your teeth are concerned, I would recommend a watch and wait on tooth #''' + WaitAndWatchToothNumberPara + '''.  If we note any indication for treatment, we will let you know and treat it accordingly.
 
    '''
    
    RestorativeTreatmentPara = '''
Restorative Treatment
    
As far as your teeth are concerned, I would recommend placing restorations on teeth #’s''' + RestorativeTreatmentToothNumberPara + '''or a watch and wait on teeth #’s ''' + RestorativeTreatmentToothNumberPara + '''. These restorations can be placed with silver amalgam, tooth colored composite, and gold or porcelain materials.  My recommendations currently are to consider the silver amalgam or tooth colored composite restorations on your back teeth and composite restorations on the front teeth.  The fees for the restorations range from $195 - $425 per tooth.  

    '''

    CrownTreatmentPara = '''
Crown Treatment

Teeth #’s''' + CrownTreatmentNumberPara + ''' have been recommended for crown treatment. Many times, your teeth may require posts and buildups for additional support. The fees for posts and build-ups are $400-550 per tooth, the fee for crowns is $1575 per tooth and the fee for a diagnostic wax-up is $175 per crown.

    '''

    RootCanalTreatmentPara = '''
Root Canal Treatment

Teeth #''' + RootCanalTreatmentNumberPara + ''' have been recommended for endodontic or root canal treatment.  The fees for this are $1200 - $1600 per tooth and the appointments could take between 1 – 4 visits.  Once root canal treatment is complete, many times, your teeth may require posts, build-ups, and crowns for additional support.  The fees for posts and build-ups are $400-550 per tooth, the fee for crowns is $1575 per tooth and the fee for a diagnostic wax-up is $175 per crown.
    
    '''

    WisdomTeethPara = '''
Wisdom Teeth    

Many patients generally find it difficult to keep their wisdom teeth clean and therefore they usually become decayed and infected.  I would therefore recommend the extraction of your wisdom teeth, teeth #''' + WisdomTeethNumberPara + ''' before they give you any problems.  The fees for the extractions range from $195 - $650 per tooth depending on the difficulty of the extraction.  An alveoplasty is often needed to recontour the bone after extractions the fee for this is $175 per tooth and $850 per quadrant (upper right, lower right, upper left and lower left).  Additional teeth that are recommended for extraction are #’s''' + WisdomTeethNumberPara +  ''' .  

    '''

    WaitAndWatchOnWisdomTeethPara = '''
Wait and Watch on Wisdom Teeth

Many patients generally find it difficult to keep their wisdom teeth clean and therefore they usually become decayed and infected.  I would therefore recommend a wait and watch on your wisdom teeth, teeth #''' + WaitAndWatchOnWisdomTeethNumberPara + '''. If we note any indication for treatments, we will let you know and treat them accordingly. The fees for the extractions range from $195 - $650 per tooth depending on the difficulty of the extraction.  An alveoplasty is often needed to recontour the bone after extractions the fee for this is $175 per tooth and $850 per quadrant (upper right, lower right, upper left and lower left).  Additional teeth that are recommended for extraction are #’s ''' + WaitAndWatchOnWisdomTeethNumberPara + '''.  

    '''

    ReplacingMissingTeethPara = '''
Replacing Missing Teeth

Once the above treatment is complete, I would recommend that you consider replacing your missing teeth with options including selective fixed bridge treatment, selective implants or removable partial dentures or full dentures.  If you are interested in any of these options, please let us know and we can discuss them in more detail at a future appointment.

    '''

    ExtractionTreatmentPara = '''
Extraction Treatment

Teeth #’s ''' + ExtractingTreatmentNumberPara + ''' have been recommended for extraction treatments. The fees for the extractions range from $195 - $650 per tooth depending on the difficulty of the extraction.  An alveoplasty is often needed to recontour the bone after extractions the fee for this is $175 per tooth and $850 per quadrant (upper right, lower right, upper left and lower left). In some cases it is recommended to place a bone graft in the extraction site and the fee for that is $550. 

    '''


    DiagnosticInformationPara = '''
Diagnostic Information 

As part of the process of developing your treatment plan, we may need to gather diagnostic information.  This may include but not limited to models of your mouth, diagnostic photographs, an ICAT scan, and a full mouth evaluation.  The fee for this is from $515 - $818.  The ICAT scan offers a 3-D view of an area which can be very valuable in planning your treatment plan by reducing risk and anticipate problems.  

    '''

    SedationDentistryPara = '''
Sedation Dentistry

For some or all aspects of your treatment, you may be interested in sedation dentistry.  We offer several levels of sedation, nitrous, oral, IV, and hospital sedation.  Generally nitrous provides the lightest, while hospital sedation is the deepest.  Most patients inquire about IV sedation which induces a state of deep relaxation and a feeling of not being bothered by what’s going on.  Many times, patients experience retrograde amnesia and do not remember their experience.  For this procedure, we are requiring that everything is planned ahead of time for your dental treatment.  We require that you have nothing to eat or drink at least 8 hours prior to the IV sedation and that you are driven to and from your appointment by a responsible adult.  We also require that someone is able to care for you at home for several hours after the appointment.  The fee for the procedure is $550 for the first hour and $100 for each 15 minutes following.   We also offer oral and inhalation sedation and the fee’s range from $160 - $395.  As with any sedation risk, death can and should be considered.  

The use of sedation should not be taken lightly in your consideration.  For our most seriously ill patient or most apprehensive patient, we also can offer general anesthesia at the area hospitals, such as Baystate Medical Center, Baystate Mary Lane Hospital, and Mercy Hospital for this type of care we change $495 to do the treatment in an OR setting and our fees for treatment are the same as our office fees.  Please keep in mind, you will accrue additional cost by the hospital, which will be your responsibility.  You must also obtain history and physical.  Please also keep in mind for sedation patients, you must prepay for your appointment and it is non-refundable.  Most sedation patients elect this care due to fear and anxiety and, in many cases, they are prone to cancel at the last minute creating many issues for our office.  We hope you understand.  

    '''

    RadiographsPara = '''
Radiographs

As far as radiographs are concerned, I would recommend that we take a panoramic radiograph and/or a full mouth series of radiographs ever 3 – 5 years and bitewing radiographs every 1 – 2 years.  We understand that many times there is a concern regarding radiographs and radiation exposure.  At Ascent Dental Care, all our radiographs are digital to provide the lease amount of radiation.  We cannot diagnose what we do not see and in today’s health care systems, it can be considered malpractice not to have this information.  Along with this, many insurance companies will reject your dental claim without radiographs, meaning you would be responsible for the entire fee.  The fees would range from $50 - $550.
    
    '''

    VELscopePara = '''
Other Treatments and Services
VELscope

Ascent Dental Care is proud to offer its patients VELscope, which is an innovative device that helps detect early abnormal tissue changes such as oral cancer and other tissue disease.  VELscope is a quick, painless procedure which scans your mouth for any changes that sometimes is not visible to the naked eye.  The fee for the VELscope is $20 and takes 2 -3 minutes to scan and evaluate your mouth.

    '''

    PerioProtectPara = ''' 
Perio Protect

As an adjunct or alternative to conventional periodontal therapy, we also offer Perio Protect for that patient who may benefit from this care, for those who don’t need it, we would just like to make you aware of the option. The Perio Protect is a non-invasive, comfortable method to treat periodontal disease.  It utilizes an antimicrobial medication that is compatible with your body’s natural defense mechanisms to infection. Medications are applied by you, at home, using custom-made trays that are similar to mouth guards, but specifically made to treat gum disease.  The trays form a seal over your teeth to direct the medication to the source of the infection.  You will wear the trays for just minutes a day during treatment.  The total fee for the Perio Protect program is $400 per arch.

    '''
    
    OcclusalGuardPara = '''
Occlusal Guard

An occlusal guard will offset pressure on your teeth and provide longevity to your existing teeth and restorations. It may also help to alleviate jaw muscle aches associated with grinding all night. The fees for an occlusal guard ranges from $200-600 depending on your insurance.

    '''

    OrthodonticTreatmentPara = '''
Orthodontic Treatment

At Ascent Dental care, we offer orthodontic treatment.  The fee for an orthodontic workup is $300-600 and it involves taking x-rays, models, photos, and performing a full orthodontic evaluation.  Seven to fourteen days later, we hope to provide you with a consultation regarding your treatment options.  If you opt to go ahead with orthodontic care with our office, this orthodontic workup fee would be credited towards your orthodontic care.  The total fee for orthodontic care can range from $3,000 to $6,600.

    '''

    TeethWhiteningPara = '''
Teeth Whitening

I would like to mention that as a selective measure, our office offers different whitening systems.  We offer whitening through Opalescence BOOST which is a powerful, effective whitening system that usually takes 1-2 hours to complete in the office. The in-office system is $450 and includes an Opalescence Go take-home kit so you can touch up as needed at home.  If you prefer to whiten on your own time, the Opalescence Go take-home kit is available for purchase at $150.  For patients who had custom trays previously, we will continue to sell the Opalescence refills for $59.99

*Please note that any whitening system you choose will only change the shade of your natural teeth and will not affect your fillings or crowns.  We have also learned that tooth whitening, although very safe, is used correctly, can cause sensitivity on your teeth and gums.  You should also be aware that there is no guarantee you will be happy with the results; we can’t predict how white teeth will get or how long the teeth will stay white.  In many cases, you will need to redo procedures every few months depending on diet and smoking and other factors.  If you are interested in any of these options, please let us know.

    '''

    InformationOnBotoxDermafilPara = '''
Information On Botox and Dermafil

Botox and Dermafil can help patients control their bruxism and grinding, can help patients who have chronic headaches that are muscle related, can help patients who have not responded to TMJ treatment and can also help patients reduce facial wrinkles and creases in the forehead, around the eyes, lips, and neck area.  The duration of treatment is approximately 4 – 9 months. The fee for Botox is $15 per unit. A consultation is required and will determine how many units are required for your desired results.  The fee for the consultation is between $45 - $200 and can be applied to the overall cost of the treatment if the patient goes forward with care.

Botox and Dermafil can help patients control their bruxism and grinding, can help patients who have chronic headaches that are muscle related, can help patients who have not responded to TMJ treatment and can also help patients reduce facial wrinkles and creases in the forehead, around the eyes, lips, and neck area.  The duration of treatment is approximately 4 – 9 months. The fee for Botox is $15 per unit. A consultation is required and will determine how many units are required for your desired results.  The fee for the consultation is between $45 - $200 and can be applied to the overall cost of the treatment if the patient goes forward with care.
    '''

    PaymentOptionsPara = '''
    
1) Cash or Check
2) Visa, MasterCard, Discover, or American Express
3) CareCredit – monthly payment plan with interest free options.
4) Ascent Dental Care is proud to provide you with the best value and care available in dentistry today.  We will be more than happy to match or improve on any fee in a written treatment plan letter presented tour office.  We are also happy to provide a guarantee to our patients on all treatment which has been recommended by our office for a period of 3 years.  We will be more than happy to replace or redo that treatment at “no charge” to the patient, providing it is the treatment that has been recommended by or office. 
5.) For additional information please visit our website at www.ascentdentalcare.com

    '''

    FinalPara = '''
Ascent Dental Care is a patient-centered practice that is focused on helping you achieve the healthiest and most beautiful smile and face. Our primary goal is that you will have such a great experience with us that you will not be able to help but tell your family and friends!

Here at Ascent Dental Care, we offer a wide array of services for both children and adults so you and your family can have all your dental needs completed under one roof.  We offer better care, better service, and better results.

    '''

    ServicesPara = '''
Here are a list of services we provide:

-Routine hygiene appointments
-Digital radiographs
-Oral cancer screening
-Restorations
-Extractions including wisdom teeth
-Endodontics
-Periodontics
-Dentures and same day Denture and partial denture repairs
-Cosmetic dentistry
-Crown and bridge with option to be completed in one appointment
-Dental implants
-Orthodontics
-Teeth whitening: in office or take home
-Sedation options: Orla sedation, inhalation sedation, IV sedation and general anesthesia
-Botox and Derma-Fillers
-Special needs patient care, hospital visits and home visits
    '''

    print(GlobalIntro)
    document.merge(Letter=GlobalIntro)
    if WaitAndWatchVariable == 1:
        print(WaitAndWatchPara)
        document.merge(WaitAndWatch=str(WaitAndWatchPara))
    if RestorativeTreatmentVariable == 1:
        print(RestorativeTreatmentPara)
        document.merge(RestorativeTreatment=str(RestorativeTreatmentPara))
    if CrownTreatmentVariable == 1:
        print(CrownTreatmentPara)
        document.merge(CrownTreatment=str(CrownTreatmentPara))
    if RootCanalTreatmentVariable == 1:
        print(RootCanalTreatmentPara)
        document.merge(RootCanal=str(RootCanalTreatmentPara))
    if WisdomTeethVariable == 1:
        print(WisdomTeethPara)
        document.merge(WisdomTeeth=str(WisdomTeethPara))
    if WaitAndWatchOnWisdomTeethVariable == 1:
        print(WaitAndWatchOnWisdomTeethPara)
        document.merge(WaitAndWatchOnWisdomTeeth=str(WaitAndWatchOnWisdomTeethPara))
    if ExtractingTreatmentVariable == 1:
        print(ExtractionTreatmentPara)
        document.merge(ExtractionTreatment=str(ExtractionTreatmentPara))



    print(DiagnosticInformationPara)
    document.merge(DiagnosticInformation=DiagnosticInformationPara)
    print(SedationDentistryPara)
    document.merge(SedationDentistry=SedationDentistryPara)
    print(RadiographsPara)
    document.merge(Radiographs=RadiographsPara)    
    print(VELscopePara)
    document.merge(VELscope=VELscopePara)    
    print(PerioProtectPara)
    document.merge(PerioProtect=PerioProtectPara)    
    print(OcclusalGuardPara)
    document.merge(OcclusalGuard=OcclusalGuardPara)    
    print(OrthodonticTreatmentPara)
    document.merge(OrthodonticTreatment=OrthodonticTreatmentPara)    
    print(TeethWhiteningPara)
    document.merge(TeethWhitening=TeethWhiteningPara)    
    print(InformationOnBotoxDermafilPara)
    document.merge(InformationOnBotoxDermafil=InformationOnBotoxDermafilPara)    
    print(PaymentOptionsPara)
    document.merge(PaymentOptions=PaymentOptionsPara)    
    print(FinalPara)
    document.merge(Closing=FinalPara)    
    print(ServicesPara)
    document.merge(Services=ServicesPara)    

    document.write(NameVar + ' letter.docx')

def exit(): 
    root.destroy()

BlankSpacer5 = Label(text='')
BlankSpacer5.pack()

MainSubmit = Button(root, text='Submit', fg='Green', command=submit)
MainSubmit.pack()

DoubleClick = Label(text='*Double Click The Submit Button!*', fg='red')
DoubleClick.pack()

CloseApp = Label(text='*You must close the app in order to open a letter*', fg='red')
CloseApp.pack()

BlankSpacer6 = Label(text='')
BlankSpacer6.pack()


BlankSpacer7 = Label(text='')
BlankSpacer7.pack()


root.mainloop()
