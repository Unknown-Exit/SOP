from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Replace with your actual OpenAI API key
import os
openai.api_key = os.getenv('OPENAI_API_KEY')


# The full SOP content
sop_context = """
Securitas USA Standard Operating Procedures (SOP)

Table of Contents
- Access Credentials
- Actions That May Result in Warning Prior to Termination of Employment
- Attendance and Punctuality
- Bereavement Leave
- Company Property and Resources
- Confidentiality of Information
- Conflict Resolution and Grievance Procedures
- Conflicts of Interest
- Discipline and Termination Guidelines
- Dress Code and Personal Appearance
- Drug-Free Workplace
- Employee Assistance Program (EAP)
- Employee Communication and Device Use
- Employee Conduct and Discipline
- Employee Responsibilities and Rights
- Employee Support Center
- Employment Classification and Status
- Employment of Relatives and Workplace Relationships
- Employment Verification
- Family and Medical Leave Act (FMLA)
- Final Wages
- Fire Evacuation Plan
- Group Health Benefits and COBRA
- Harassment and Discrimination
- Holidays
- Involuntary Separation/Layoff
- Leave of Absence Policies
- Login Access/Alarm Access
- Making Badges
- Medical/Dental/Other Insurance
- Payroll Choices
- Possession of Firearms and Weapons
- Pregnancy Leave
- Release of Company Information/Press Inquiries
- Safeguarding of Personal Information
- Safety and Health
- Securitas Company Roster
- Securitas Electronic Pay Stub Access
- Severe Weather Plan
- Smoking Policies
- Social Media and Electronic Communication
- Special Security Devices
- Technology and Computer Use
- Telecommuting and Remote Work
- Termination of Employment
- Timekeeping and Off-the-Clock Work
- Training and Development
- Vehicle Management
- Vehicle Use and Safety
- Viega Company Manager/Supervisor Roster
- Voluntary Separation
- Workers' Compensation
- Workplace Violence

Access Credentials
Viega Address: 2211 Viega Avenue, McPherson County, Kansas 67460
Coordinates: 38.38807 N, 97.62289 W
Login Access/Alarm Access:
Data Bridge:
User: scalehouse
Password: scalehouse
Security Computer:
Password: S3cur!ty or S3cur!tas16!
Securitas Gmail:
User: SecuritasViegaCompany@gmail.com
Password: Securitas1414!
WiFi:
User: VGuest
Password: Viega1899
Obseron (Cameras):
User: Admin
Password: Jetstream
Alert Media:
First Name: Security
Last Name: Viega
Password: Securitas16!
One Drive:
User: mcpherson.security@viega.us
Password: S3cur!ty
Teams (Shack Phone):
User: mcpherson.security@viega.us
Password: 39bQoxvmNS2F
Outlook:
User: mcpherson.security@viega.us
Password: S3cur!ty
SoSpes:
User: mcpherson.security@viega.us
Password: S3cur!tas16!
ADT Alarms:
Account (2210 Building): P1352873
Password: Germany
Alt. Password: Viega McPherson
Account (2108 Building):
P1352970
Password: Germany
Alt. Password: Viega McPherson
Alarm Central:
Account (2211 Building): E1003387
Password: Germany
Alt. Password: Viega McPherson

Actions That May Result in Warning Prior to Termination of Employment
Securitas USA may, depending on the circumstances and the severity of the conduct, either issue a disciplinary warning or terminate employment for:
Inefficient or Substandard Performance: Includes inefficient or substandard performance of an assigned duty or responsibility.
Excessive Absenteeism or Tardiness: Repeated failures to report to work or return from rest periods or meal periods on time.
Failure to Report an Absence: Failure to report an absence in accordance with the attendance policy or failure to immediately report a work-related injury.
Carelessness or Negligence: Includes negligence in the performance of an assigned duty or in the care and use of Company or client property.
Unauthorized Posting: Posting of notices or other written material on Company property without prior written approval of Securitas USA.
Unauthorized Device Use: Unauthorized use of a personal pager, cellular telephone, or other personal electronic devices while on duty.
Failure to Work Overtime: Failure to work overtime when an emergency occurs.
Dress Code Violation: Repeated failure to adhere to dress code and/or grooming standards.
Violation of Chain of Command: Violation of internal chain of command (employees will not be subjected to negative treatment as a result of complaining about their wages, hours, or working conditions).
Allowing Personal Visitors: Allowing personal visitors to remain at post while on duty.
Bringing Pets to Work: Bringing pets to work (except as authorized in advance as a reasonable accommodation for a disability).
Showing Up or Socializing: Showing up or socializing at a client site when not scheduled to work.
Violation of Post Orders: Any breach of specific post orders.

Attendance and Punctuality
Regular attendance and punctuality are essential to the smooth operation of Securitas USA's business. Employees are expected to report to work on time and as scheduled, and to notify their supervisor as soon as possible if they are unable to report to work.
Absences: Absences may be excused or unexcused, depending on the circumstances. Examples of excused absences include illness, injury, or family emergencies. Examples of unexcused absences include failure to report to work without notice or approval, or repeated tardiness.
Tardiness: Employees who are late to work are expected to notify their supervisor as soon as possible and to make up the missed time if required. Repeated tardiness may result in disciplinary action, up to and including termination of employment.
No-Call, No-Show: Employees who fail to report to work without notice for three consecutive days may be considered to have abandoned their position and may be subject to termination of employment.
Documentation: Employees who are absent from work due to illness or injury may be required to provide documentation from a healthcare provider. Employees who are absent for an extended period may be required to provide periodic updates on their condition and expected return date.
Return to Work: Employees who are returning to work after an extended absence may be required to provide a fitness-for-duty certification from their healthcare provider. Employees returning from leave are expected to resume their regular duties and responsibilities as soon as possible.

Bereavement Leave
Security officers may be granted up to three consecutive workdays, without pay, unless specified by client contract or otherwise required by state or local law, following the death of an immediate family member to arrange for and/or attend the funeral or any other reasons authorized by applicable state or local law. Additional time may be requested with the approval of your supervisor. You may be required to provide necessary documentation validating family relationship, proof of death, or funeral schedule.
For the purpose of this policy, unless otherwise required by state or local law, "immediate family members" are defined as:
Mother/father – to include in-law, step, and foster parents
Brother/sister – to include in-law and step relations
Grandparent and grandchildren
Spouse
Child – to include step and foster child(ren)
Legal guardian
Domestic partner

Company Property and Resources
Securitas USA provides employees with the tools, equipment, and resources necessary to perform their job duties effectively. Employees are expected to use Company property and resources responsibly and in accordance with Company policies.
Use of Company Property: Company property, including vehicles, equipment, and office supplies, should be used only for legitimate business purposes. Employees are responsible for maintaining Company property in good condition and for reporting any damage or loss to their supervisor.
Return of Company Property: Upon termination or resignation, employees are required to return all Company property, including uniforms, identification badges, keys, and electronic devices. Failure to return Company property may result in legal action.
Personal Use of Company Resources: Employees are not permitted to use Company resources for personal gain or for activities unrelated to their job duties without prior authorization from their supervisor.

Confidentiality of Information
Employees are required to maintain the confidentiality of all proprietary and sensitive information to which they have access as part of their job duties. This includes, but is not limited to, information about the Company's clients, employees, and business operations.
Disclosure of Information: Employees are prohibited from disclosing confidential information to unauthorized individuals or entities without prior approval from their supervisor or the Legal Department.
Use of Information: Confidential information should be used only for legitimate business purposes and in accordance with Company policies and procedures.
Protection of Information: Employees are responsible for safeguarding confidential information from unauthorized access, use, or disclosure. This includes securing physical and electronic records, using strong passwords, and following Company protocols for data protection.

Conflict Resolution and Grievance Procedures
Securitas USA is committed to providing a positive and supportive work environment. Employees are encouraged to address any concerns or grievances they may have with their supervisor or Human Resources representative.
Reporting Concerns: Employees who have concerns about their work environment, treatment by supervisors or coworkers, or other issues are encouraged to report them to their supervisor or Human Resources representative as soon as possible.
Conflict Resolution: The Company will work with employees to resolve conflicts in a fair and timely manner. This may include mediation, counseling, or other appropriate measures.
Grievance Procedures: Employees who are not satisfied with the resolution of their concerns may file a formal grievance with the Human Resources Department. The grievance will be reviewed by Company management, and a decision will be made within a reasonable timeframe.

Conflicts of Interest
Employees are expected to avoid conflicts of interest that could compromise their ability to perform their job duties impartially and in the best interest of Securitas USA.
Personal Relationships: Employees should not engage in activities or relationships that could create a conflict of interest, such as accepting gifts or favors from clients, vendors, or competitors.
Outside Employment: Employees are required to disclose any outside employment or business activities that could conflict with their responsibilities at Securitas USA. Outside employment should not interfere with an employee's ability to perform their job duties or create a conflict of interest.
Financial Interests: Employees are prohibited from having a financial interest in any company or entity that does business with Securitas USA, unless prior approval is obtained from the Legal Department.

Discipline and Termination Guidelines
The following guidelines generally apply to the discipline and involuntary termination of employees. However, inasmuch as employment is "at will," these guidelines do not create any contractual or other rights for any employee. The Company may, in its discretion, choose to use or not use progressive discipline prior to termination of employment.
Actions That Warrant Immediate Termination of Employment
Below is a partial list of conduct which, depending on the circumstances and severity of conduct, warrant involuntary termination on the first occurrence. Such offenses include, but are not limited to, the following:
Physical Violence: Threatening or committing physical violence, or intimidating behavior.
Illegal Conduct: Includes discrimination or harassment.
Falsification of Records: Providing false information or false statements to management (excluding any omission of information on an employment application related to union activity).
Theft: Unauthorized taking or removal of client or Company property or the property of another person or other dishonesty.
Damage to Property: Damage to Company or client property.
Falsification of Time Records: Filling out or completing a Company time record for another person, or knowingly allowing someone else to fill out one’s own timesheet or falsification of time records, or other violation of wage and hour laws.
Possession of Weapons: Carrying or possessing weapons such as guns, dangerous devices, or other weapons on Company and/or client premises, including parking lots, without proper written authorization by Company management, and/or in violation of applicable laws.
Conviction of Crime: Conviction or pleading guilty to violation of any criminal statute or code, whether or not such a crime is committed against Securitas USA or any of its employees, when, in Securitas USA’s opinion, the conviction or guilty plea is reasonably related to the nature of the employee’s work or continued employment could jeopardize Securitas USA or client interests.
Drug or Alcohol Use: Use of or being under the influence of alcohol, intoxicants, illegal drugs, or controlled substances during work hours, or on Company or client vehicles, testing positive for illegal drugs or controlled substances (including marijuana) while following a Company drug test; violation of Drug-Free workplace policy, as permitted under applicable law.
Drug Sale or Purchase: Sale, purchase, attempted sale or purchase, possession, or transfer of intoxicants, illegal drugs, or controlled substances during work hours, or while on the job, on Company property, or in Company vehicles.
Unauthorized Absence: Leaving post without proper relief or authorization from your supervisor or “no call, no show.”
Safety Violations: Willful or repeated violation of safety rules.
Code of Business Ethics Violation: Willful or repeated violation of Company Code of Business Ethics, our Sexual Harassment Policy, or other forms of unlawful discrimination.
Failure to Participate in Investigations: Failure or refusal to participate in a lawful Company investigation.
Failure to Accept Assignments: Repeated failure to accept assignments.
Improper Vehicle Use: Unauthorized or improper use of a Company or client vehicle.
Falsification of Leave Reasons: Falsifying the reasons for a leave of absence.
Significant Violations: Significant violation of a client’s Post Orders.
Sleeping While on Duty: Sleeping while on duty, or the appearance of sleeping while on duty.
Core Values: Failing to uphold the Company core values of Integrity, Vigilance, and Helpfulness.

Dress Code and Personal Appearance
Employees are expected to maintain a professional appearance at all times while on duty. This includes wearing the appropriate uniform, maintaining personal hygiene, and adhering to the Company's grooming standards.
Uniforms: Employees are required to wear the designated uniform for their position while on duty. Uniforms should be clean, pressed, and in good condition. Employees are responsible for maintaining their uniforms and for replacing them as needed.
Grooming: Employees are expected to maintain personal hygiene and grooming standards that are consistent with the Company's image and professional standards. This includes regular haircuts, clean and trimmed nails, and appropriate use of cosmetics and fragrances.
Personal Appearance: Employees should avoid wearing excessive jewelry, tattoos, or body piercings that may be deemed unprofessional or distracting. Any visible tattoos or body piercings should be covered while on duty.

Drug-Free Workplace
Securitas USA is committed to maintaining a drug-free workplace. Employees are prohibited from using, possessing, distributing, or being under the influence of illegal drugs or controlled substances while on Company property, during work hours, or while on duty.
Drug Testing: Employees may be required to undergo drug testing as a condition of employment, after a workplace accident, or if there is reasonable suspicion of drug use. Refusal to submit to a drug test may result in disciplinary action, up to and including termination of employment.
Prescription Medications: Employees who are taking prescription medications that may impair their ability to perform their job duties must notify their supervisor and provide appropriate documentation from their healthcare provider.
Alcohol Use: Employees are prohibited from consuming alcohol while on duty, during work hours, or while on Company property. Employees who are found to be under the influence of alcohol while on duty may be subject to disciplinary action, up to and including termination of employment.

Employee Assistance Program (EAP)
In recognizing that the success of Securitas USA and our business depends upon the well-being of our employees, Securitas USA offers an Employee Assistance Program (EAP) to all full-time and part-time employees who have completed 90 days of service and their qualified dependents.
Qualified employees and family members may receive assistance in managing life’s challenges outside the workplace such as financial and credit problems, loss of a loved-one, personal relationship issues, substance abuse or dependency, concerns regarding parents or children, stress, anxiety, and any other personal circumstances that may require skilled professional help. For up to five face-to-face counseling sessions per family member, per incident, per year there is no charge to the employee. Any employee or eligible family member may obtain assistance by calling 1-855-543-6877, 24 hours per day, 7 days a week. Online member services are also available at anthemEAP.com/securitas. Access code is “securitas.”

Employee Communication and Device Use
Employees are expected to use Company communication devices, including telephones, email, and messaging systems, for business purposes only. Personal use of Company communication devices should be kept to a minimum and should not interfere with work responsibilities.
Telephone Use: Personal telephone calls should be kept to a minimum and should not interfere with work responsibilities. Employees are not permitted to make long-distance calls at the Company's expense without prior approval.
Email and Messaging Systems: Employees are expected to use Company email and messaging systems for business purposes only. Personal use of email and messaging systems should be kept to a minimum and should not interfere with work responsibilities. Employees are prohibited from using Company email or messaging systems to send inappropriate, offensive, or confidential information.
Social Media: Employees are not permitted to use Company computers or communication devices to access social media sites for personal use during work hours. Employees are also prohibited from posting confidential or proprietary information about the Company, its clients, or its employees on social media sites.

Employee Conduct and Discipline
Employees are expected to conduct themselves in a professional manner at all times while on duty. This includes adhering to Company policies and procedures, treating coworkers and clients with respect, and maintaining a positive attitude.
Professionalism: Employees are expected to maintain a professional demeanor while on duty. This includes using appropriate language, dressing in a professional manner, and treating coworkers and clients with respect.
Teamwork: Employees are expected to work collaboratively with their coworkers and supervisors to achieve Company goals. This includes being open to feedback, communicating effectively, and supporting one another in the workplace.
Compliance: Employees are expected to comply with all Company policies and procedures, as well as applicable laws and regulations. Failure to comply with Company policies or legal requirements may result in disciplinary action, up to and including termination of employment.

Employee Responsibilities and Rights
Employees have the responsibility to perform their job duties to the best of their ability, to adhere to Company policies and procedures, and to treat coworkers and clients with respect. Employees also have the right to a safe and healthy work environment, fair treatment, and equal opportunity for advancement.
Job Performance: Employees are expected to perform their job duties to the best of their ability, to meet or exceed performance standards, and to take responsibility for their work. Employees who fail to meet performance standards may be subject to disciplinary action, up to and including termination of employment.
Workplace Safety: Employees have the right to a safe and healthy work environment, free from hazards and unsafe conditions. Employees are encouraged to report any safety concerns to their supervisor or Human Resources representative.
Fair Treatment: Employees have the right to be treated fairly and with respect by their coworkers and supervisors. The Company is committed to providing a work environment that is free from discrimination, harassment, and retaliation.
Equal Opportunity: Employees have the right to equal opportunity for advancement based on their performance, qualifications, and abilities. The Company is committed to providing equal employment opportunities to all employees, regardless of race, color, religion, sex, national origin, age, disability, or any other protected characteristic.

Employee Support Center
To better support you with issues or questions related to your employment, systems, and processes, you have access to the Employee Support Center (ESC). Employee Support Center Representatives will be able to assist you in real-time or will route your inquiry to a subject matter expert who will be able to quickly provide resolution.
You can access the Employee Support Center Monday through Friday, 8 a.m. to 11 p.m. Eastern Standard Time.
Access by phone: 866-864-3375, select option 2 (HR & Payroll)
Access via the Securitas Employee Portal: https://employee.securitassinc.com/#/
Access via the OneID portal: https://oneid.securitassinc.com/
Access by mobile device of non-Securitas PC: https://securitassd.service-now.com/sp

Employment Classification and Status
Employees are classified based on their job duties, hours worked, and other factors. These classifications determine eligibility for certain benefits and other terms and conditions of employment.
Full-Time Employees: Employees who are regularly scheduled to work 30 or more hours per week are classified as full-time. Full-time employees are eligible for Company benefits, including health insurance, paid time off, and retirement plans.
Part-Time Employees: Employees who are regularly scheduled to work less than 30 hours per week are classified as part-time. Part-time employees may be eligible for certain benefits, such as retirement plans, but may not be eligible for other benefits, such as health insurance.
Temporary Employees: Employees who are hired for a specific project or period of time are classified as temporary. Temporary employees are not eligible for Company benefits, unless required by law.
Exempt and Non-Exempt Employees: Employees are classified as exempt or non-exempt based on their job duties and compensation. Exempt employees are not eligible for overtime pay, while non-exempt employees are eligible for overtime pay in accordance with applicable laws.

Employment of Relatives and Workplace Relationships
Securitas USA recognizes that employees may have personal relationships with other employees, including family members, romantic partners, and friends. The Company does not prohibit these relationships but does require that they be conducted in a professional manner that does not interfere with work responsibilities or create a conflict of interest.
Employment of Relatives: Employees may be employed in the same department or work area as a relative, provided that the relationship does not create a conflict of interest or interfere with work responsibilities. However, employees who are related may not work in a direct supervisory relationship with one another.
Romantic Relationships: Employees who are in a romantic relationship with another employee are expected to conduct themselves in a professional manner at all times while on duty. Romantic relationships between supervisors and subordinates are strongly discouraged and may be prohibited if they create a conflict of interest or interfere with work responsibilities.
Workplace Conduct: Employees who are involved in a personal relationship with another employee are expected to maintain a professional demeanor while on duty. Any conduct that is disruptive, unprofessional, or creates a conflict of interest may result in disciplinary action, up to and including termination of employment.

Employment Verification
Securitas USA provides employment verification for current and former employees upon request. Employment verification may be required for various purposes, including loan applications, rental agreements, and government programs.
Requests for Employment Verification: Requests for employment verification should be directed to the Human Resources Department. Employees may be required to provide written authorization for the release of employment information.
Verification of Employment: The Company will verify employment by providing information such as the employee's job title, dates of employment, and salary. The Company will not disclose personal information, such as Social Security numbers or home addresses, without the employee's consent.
Employment References: The Company may provide employment references for current or former employees upon request. References will be provided in accordance with Company policies and applicable laws.

Family and Medical Leave Act (FMLA)
Securitas USA complies with the Family and Medical Leave Act (FMLA) and applicable state laws regarding leave for employees with qualifying medical or family-related conditions.
Eligibility: Employees who have worked for the Company for at least 12 months and have worked at least 1,250 hours during the previous 12 months are eligible for FMLA leave. Eligible employees may take up to 12 weeks of unpaid leave in a 12-month period for certain qualifying reasons, such as the birth or adoption of a child, the serious health condition of the employee or a family member, or qualifying exigencies related to military service.
Requesting Leave: Employees who wish to take FMLA leave must notify their supervisor and the Human Resources Department as soon as possible. Employees may be required to provide medical certification or other documentation to support their request for leave.
Return to Work: Employees who take FMLA leave are entitled to return to their same or an equivalent position upon their return to work. Employees who are unable to return to work at the end of their FMLA leave may be eligible for additional leave or other accommodations, depending on the circumstances.

Final Wages
Your final paycheck will be provided to you as required by applicable state law.

Fire Evacuation Plan
Securitas USA is committed to the safety and well-being of its employees and clients. In the event of a fire or other emergency, employees are expected to follow the Company's fire alarm and fire evacuation plan.
Initial Response:
If a fire alarm is triggered, notify Security immediately.
Call 9-1-1 from a landline or cell phone to report the fire.
Notify Security and Leadership:
Identify the location and direction of the fire to Emergency Responders.
Notify building leadership immediately, who will initiate the evacuation process.
Notification to Employees:
Evacuation orders will be communicated through:
Air horn blasts (repeated twice).
Overhead PA System/Alarms.
Direct communication from leadership.
Evacuation Procedure:
Redirect building occupants to stairs and exits away from the fire.
Ensure all injured persons receive medical attention immediately.
Guide employees and visitors to the primary assembly location.
Supervisors must account for all personnel on their roster.
Post-Evacuation Actions:
EHS Security will brief the Fire Department Incident Commander (IC) on the situation.
If necessary, building leadership will coordinate the relocation of evacuated personnel.
Final Considerations:
Ensure all personnel are informed about the emergency evacuation plan.
Keep evacuation routes and assembly areas clear at all times.

Group Health Benefits and COBRA
Your health benefits will terminate at the time of separation in accordance with that plan’s coverage contract. In most instances, you may continue basic health benefits under the Consolidated Omnibus Budget Reconciliation Act (COBRA). Information regarding COBRA will be sent to your address on record with Securitas USA after the Securitas USA Benefits Department receives notification from your local office of your separation. If you do not receive information regarding COBRA within 14 days of the time of your separation, please contact your local Human Resources representative.

Harassment and Discrimination
Securitas USA is committed to providing a work environment that is free from harassment and discrimination. Employees are expected to treat their coworkers and clients with respect and dignity at all times.
Prohibited Conduct: Harassment and discrimination of any kind, including but not limited to, based on race, color, religion, sex, national origin, age, disability, or any other protected characteristic, is strictly prohibited. This includes verbal, physical, and visual conduct that creates a hostile or offensive work environment.
Reporting Harassment and Discrimination: Employees who believe they have been subjected to harassment or discrimination should report the incident to their supervisor, Human Resources representative, or the Company's Ethics Hotline. The Company will investigate all reports of harassment and discrimination and will take appropriate corrective action if necessary.
Retaliation: The Company prohibits retaliation against employees who report harassment or discrimination or who participate in an investigation of such reports. Employees who believe they have been retaliated against should report the incident to their supervisor, Human Resources representative, or the Company's Ethics Hotline.

Holidays
Holiday schedules vary depending upon your client site. Normally you will not be paid for the holiday unless you work on that day.

Involuntary Separation/Layoff
There are certain times when it may become necessary to lay off employees as a result of changing business conditions. Examples of these conditions include but are not limited to:
Reduction in work force.
Loss of client contract.
Reorganization resulting in the elimination or modification of a job.
When Securitas USA concludes that a layoff or reduction in force is necessary or appropriate, the positions and/or employees to be eliminated will be selected based on a number of factors, which may include demonstrated performance and skills, ability and reliability, and seniority.

Leave of Absence Policies
Securitas USA provides several types of leaves of absence to employees for various reasons, including medical, family, and personal reasons. All leaves of absence are subject to Company policies and applicable laws.
Medical Leave: Securitas USA will grant an unpaid leave of absence for employees who are not FMLA eligible, but who need a temporary leave of absence as a reasonable accommodation under the ADA, unless the leave would pose an undue hardship for the Company. A doctor’s certification will be required validating the need for time off for treatment of a medical condition.
State Family Rights Act Leave: Some states have enacted their own Family Rights Act leave laws with separate qualifications and provisions. Securitas USA complies with all applicable state as well as federal laws in all instances where they apply. For specific information regarding leave eligibility qualifications and benefits, contact your local Human Resources representative or manager.
Personal Leaves of Absence: Securitas USA may grant a leave of absence for justifiable reasons for periods not to exceed 30 consecutive calendar days for employees who have had at least 12 months of continuous service. Your local branch management has full discretion and makes the final authorization in granting any leave of absence. However, if for any reason the leave has been misrepresented or business needs require your return to work, the leave may be canceled.
Paid Family Leave: According to applicable state law, you may be eligible for paid family leave, which generally is a form of partial wage replacement provided by the state where an employee is on a leave of absence for certain reasons, such as caring for a new child or family member with a serious health condition. Please check with your HR Representative for more information.
Military Leave: Securitas USA will comply with all applicable federal and state laws regarding military leave of absence and returning veterans’ re-employment rights.
Jury and Witness Duty: A leave of absence resulting from jury duty or testifying as a subpoenaed witness will be granted in accordance with federal, state, and local laws. You will be granted an unpaid leave of absence (unless applicable law requires payment, in which case we will follow applicable law) for this purpose, provided a notice is presented to your supervisor. When practical, you should continue to report to work on days when you do not report for jury duty. It is your responsibility to return to work immediately following the expiration of jury or witness duty. If you are required to testify as a witness in a Securitas USA-related case, or on behalf of a client, you will receive your appropriate wage for the period of time required by the legal proceedings. All current employee benefits will continue while you are on jury or witness duty leave.
Bereavement Leave: Security officers may be granted up to three consecutive workdays, without pay, unless specified by client contract or otherwise required by state or local law, following the death of an immediate family member to arrange for and/or attend the funeral or any other reasons authorized by applicable state or local law. Additional time may be requested with the approval of your supervisor. You may be required to provide necessary documentation validating family relationship, proof of death, or funeral schedule.
Other Time Off: Securitas USA understands that you may occasionally need time off from work to address personal matters. Unless otherwise required by law, requests for time off will be evaluated according to business necessity, scheduling needs, and management discretion. Securitas USA will comply with its legal obligations under applicable state laws by providing you time off, where necessary, to vote, to perform emergency duty as a volunteer firefighter, to appear at your child’s school or for certain school activities, pursuant to court requests of the school, to attend an adult literacy education program, or in accordance with any state and/ or federal laws. Time off that is provided under this policy will ordinarily be unpaid except where the law requires that it be compensated.

Login Access/Alarm Access
Data Bridge:
User: scalehouse
Password: scalehouse
Security Computer:
Password: S3cur!ty or S3cur!tas16!
Securitas Gmail:
User: SecuritasViegaCompany@gmail.com
Password: Securitas1414!
WiFi:
User: VGuest
Password: Viega1899
Obseron (Cameras):
User: Admin
Password: Jetstream
Alert Media:
First Name: Security
Last Name: Viega
Password: Securitas16!
One Drive:
User: mcpherson.security@viega.us
Password: S3cur!ty
Teams (Shack Phone):
User: mcpherson.security@viega.us
Password: 39bQoxvmNS2F
Outlook:
User: mcpherson.security@viega.us
Password: S3cur!ty
SoSpes:
User: mcpherson.security@viega.us
Password: S3cur!tas16!
ADT Alarms:
Account (2210 Building): P1352873
Password: Germany
Alt. Password: Viega McPherson
Account (2108 Building):
P1352970
Password: Germany
Alt. Password: Viega McPherson
Alarm Central:
Account (2211 Building): E1003387
Password: Germany
Alt. Password: Viega McPherson

Making Badges
Employees are required to wear identification badges at all times while on duty. Identification badges are used to verify employee identity and to access certain areas of Company property.
Loading the Badge Machine:
Locate the black badge machine in the office.
Open the compartment where blank IDs are stored.
Load the machine with white blank IDs.
Printing the Front of the Badge:
Open the badge printing software.
Upload the front image file (Viega logo).
Adjust image size and position, then start the print process.
Printing the Back of the Badge:
Re-insert the badge with the blank side facing up.
Upload the back image file (Values).
Adjust image size and position, then start the print process.
Printing the Employee Image and Name:
Open the Administration Station software.
Upload the employee's photo, adjust, and print.
Verifying and Finalizing the Badge:
Inspect the badge to ensure proper print quality.
Place the finished badge into a laminated pocket.
Adding Security Team Information:
Print a separate paper with security team info and place it behind the badge.
Updating Employee Information:
Open Administration Station, search for the employee, and update their profile.
Creating a New Badge:
If no badge exists, create one following the steps outlined in the Administration Station.
Troubleshooting Tips:
If the machine jams, carefully remove any stuck IDs.
If the print quality is poor, check ink levels and clean print heads.

Medical/Dental/Other Insurance
Health Insurance
Benefit programs vary by location, client contract, and applicable state law. Check with your local Human Resources representative for information on programs applicable to you. You may also consult the governing Summary Plan Description (SPD) for further plan and specific coverage information.
Life Insurance
Securitas USA generally provides group term life insurance in the amount of $10,000 for all full-time (30 hours or more per week) security officers, who have been employed for more than 90 days. In some cases, additional insurance may be available. Contact your local Human Resources representative for further details.
Medical/Dental/Other Insurance (Client Site Specific)
Certain locations and client contracts provide partially subsidized insurance coverage for security officers and in some instances for immediate family members, as well. Your local office will inform you of any plans that may apply to you and will provide coverage and enrollment information. If you have questions, please contact your local Human Resources representative or your District Manager.
Employee-Paid Voluntary Benefits
Securitas USA provides employees with the opportunity to enroll in various voluntary benefit plans, depending upon location, for which the employee pays the full premium amount via authorized payroll deduction. See your local Human Resources representative for more information or to enroll in any of these plans.
Employee Responsibility for Premium Contributions
When an employee temporarily ceases to make timely payments for their health insurance premium contributions, either through direct payment or payroll deductions, that health insurance coverage is subject to cancellation of coverage and loss of benefits. Employees on approved leaves of absence are responsible for premium contributions. Depending on the type of leave, deductions may not be able to be taken directly while on leave. In this case, arrangements may be made for retroactive payments to be made upon return to employment. Certain leave benefits may be canceled in compliance with current regulations after a period of time. If applicable, you will be offered COBRA upon termination of benefits. Once you return to active duty your benefits can be reinstated although specific plans and premiums may differ depending upon assignment. Please contact your local Human Resources representative for more information.

Payroll Choices
Under the Payroll Choices Program, and where allowed by state law, Securitas USA offers two options to receive your pay; either by Direct Deposit, or a personalized and secure Visa @ Payroll Card, provided by Wisely. With direct deposit, you can select the bank account(s) of your choice, while the Payroll Card requires no bank accounts. Advantages of Direct Deposits:
Choose your own bank
Deposit funds in up to three separate accounts
No lost checks or delivery delays
No check cashing fees

Possession of Firearms and Weapons
Securitas USA prohibits employees from carrying, possessing, or using firearms, weapons, or dangerous devices while on Company or client property, during work hours, or while on duty. This includes but is not limited to firearms, knives, explosives, and chemical weapons.
Prohibited Conduct: Employees are prohibited from carrying, possessing, or using firearms, weapons, or dangerous devices while on Company or client property, during work hours, or while on duty. This includes but is not limited to firearms, knives, explosives, and chemical weapons.
Exceptions: Employees who are required to carry a firearm as part of their job duties may do so only if they have obtained the appropriate permits and have completed the required training. Employees who are authorized to carry a firearm must follow all Company policies and procedures regarding the use and storage of firearms.
Disciplinary Action: Employees who violate this policy may be subject to disciplinary action, up to and including termination of employment. In addition, employees who violate this policy may be subject to criminal prosecution.

Pregnancy Leave
Securitas USA complies with the Pregnancy Discrimination Act, Pregnant Workers Fairness Act, FMLA, ADA, and all relevant Federal, state, and local laws with respect to leaves of absence for pregnant employees/employees disabled by pregnancy or pregnancy-related conditions.

Release of Company Information/Press Inquiries
Employees are not authorized to release Company information to the press or other external parties without prior approval from their supervisor or the Legal Department. This includes but is not limited to information about the Company's clients, employees, business operations, and financial performance.
Press Inquiries: Employees who receive inquiries from the press or other external parties should refer them to the Legal Department or the designated Company spokesperson. Employees are not authorized to speak on behalf of the Company or to provide information about the Company's clients, employees, business operations, or financial performance without prior approval.
Confidential Information: Employees are prohibited from disclosing confidential information about the Company, its clients, employees, or business operations to unauthorized individuals or entities. This includes but is not limited to information about the Company's financial performance, business strategies, client relationships, and employee compensation.

Safeguarding of Personal Information
Employees are responsible for safeguarding personal information from unauthorized access, use, or disclosure. This includes securing physical and electronic records, using strong passwords, and following Company protocols for data protection.
Confidentiality: Employees are required to maintain the confidentiality of all personal information to which they have access as part of their job duties. This includes but is not limited to information about the Company's clients, employees, and business operations.
Data Protection: Employees are responsible for protecting personal information from unauthorized access, use, or disclosure. This includes securing physical and electronic records, using strong passwords, and following Company protocols for data protection.
Reporting Breaches: Employees who become aware of a breach of personal information should report it to their supervisor or the Legal Department immediately. The Company will investigate all reports of data breaches and will take appropriate corrective action if necessary.

Safety and Health
Securitas USA is committed to providing a safe and healthy work environment for its employees. Employees are expected to follow all Company safety and health policies and procedures, and to report any unsafe conditions or practices to their supervisor immediately.
Safety Procedures: Employees are expected to follow all Company safety procedures, including but not limited to, wearing appropriate personal protective equipment, following proper lifting techniques, and using equipment safely and correctly.
Health Procedures: Employees are expected to follow all Company health procedures, including but not limited to, maintaining personal hygiene, washing hands regularly, and reporting any symptoms of illness to their supervisor immediately.
Reporting Injuries: Employees who are injured on the job should report the injury to their supervisor immediately. The Company will provide medical treatment and workers' compensation benefits in accordance with applicable laws and Company policies.
Workers' Compensation: Securitas USA has Workers’ Compensation insurance coverage, as required by law, to protect employees who are injured on the job. This insurance provides medical, surgical, and hospital treatment in addition to payment for loss of earnings that result from work-related injuries. The cost of this coverage is paid by Securitas USA.
Reporting Injuries: If you are injured while working, you must report the incident to your supervisor within a reasonable period of time, proportionate to the seriousness of the injury or illness, regardless of how minor the injury or illness may be. If you have any questions regarding the Workers’ Compensation Insurance Program, please contact your branch office.

Securitas Company Roster
The Company maintains a roster of all employees, including their job titles, contact information, and emergency contacts. The roster is used for communication purposes, emergency response, and other administrative functions.
Updating Information: Employees are responsible for keeping their contact information and emergency contacts up to date. Changes should be reported to the Human Resources Department immediately.
Access to Roster: The Company roster is confidential and is accessible only to authorized personnel. Employees are not permitted to access or distribute the roster without prior approval.
Emergency Contacts: Employees are required to provide emergency contact information to the Company. This information will be used in the event of an emergency to notify the employee's designated contacts.

Securitas Electronic Pay Stub Access
Securitas USA offers convenient access to view and print your pay stubs online through Oracle each pay day. You may retrieve pay stubs from Equifax Paperless Pay: https://paperlesspay.talx.com/securitas for payroll cycles prior to September 30, 2020. All pay statements after September 30, 2020, are retrievable within the Oracle system. To access your pay stubs online, go to www.securitasepay.com. Or call 866-604-EPAY (3729) to review your pay information.
Access to payroll detail 24 hours a day, 7 days a week, by web, phone & fax
Access to paycheck history for up to 3 years
Access to paycheck detail the day before payday
Ability to view pay stubs through the web, phone, and to print, if applicable
For more details on this service, contact your local branch office. Depending on state law, employees who wish to have paper paycheck stubs printed and provided weekly by the Company may do so by contacting Human Resources or their branch office. Employees may also use a Company computer and/or printer at their branch office for the purpose of viewing and printing the pay stubs and/or may request copies of the paycheck stubs. Any employee who has difficulty accessing their paycheck stubs should contact Human Resources.

Severe Weather Plan
Preparation:
Designated monitors track the weather for potential severe conditions.
EHS, along with Managers and Security, review protocols and ensure preparedness.
Shelter Activation:
Severe weather expected in the area.
McPherson City Storm Sirens activate.
Leadership determines the need based on the situation.
Notification Methods:
Air Horn: 3 short blasts, repeated twice.
Overhead PA System.
Direct communication from Leadership.
Shelter Procedure:
Employees move quickly to designated Severe Weather Shelter areas.
Employees with Digital Radios should bring them to the shelter area.
Supervisors conduct headcounts and report to EHS/Security.
Post-Shelter Actions:
All employees remain in the shelter until an all-clear is issued.

Smoking Policies
Securitas USA maintains a smoke-free work environment. Smoking is prohibited in all Company buildings, vehicles, and on Company property, except in designated smoking areas.
Designated Smoking Areas: Employees who smoke may do so only in designated smoking areas. Smoking is not permitted in Company buildings, vehicles, or on Company property, except in designated smoking areas
Designated Smoking Areas: Employees who smoke may do so only in designated smoking areas. Smoking is not permitted in Company buildings, vehicles, or on Company property, except in designated smoking areas.
Compliance with Local Laws: Employees are expected to comply with all local laws and regulations regarding smoking in the workplace. This includes but is not limited to, laws prohibiting smoking in certain areas, restrictions on smoking near entrances or exits, and requirements for the posting of "No Smoking" signs.
Enforcement: Employees who violate the Company's smoking policies may be subject to disciplinary action, up to and including termination of employment. Employees who are found to be smoking in non-designated areas or who are in violation of local smoking laws may also be subject to fines or other legal penalties.

Social Media and Electronic Communication
Employees are expected to use social media and electronic communication in a responsible and professional manner. The Company's policies on social media and electronic communication apply to all employees, both on and off duty.
Social Media Use: Employees are not permitted to use Company computers or communication devices to access social media sites for personal use during work hours. Employees are also prohibited from posting confidential or proprietary information about the Company, its clients, or its employees on social media sites.
Electronic Communication: Employees are expected to use electronic communication devices, including email and messaging systems, for business purposes only. Personal use of electronic communication devices should be kept to a minimum and should not interfere with work responsibilities. Employees are prohibited from using electronic communication devices to send inappropriate, offensive, or confidential information.
Professional Conduct: Employees are expected to conduct themselves in a professional manner when using social media and electronic communication devices. This includes but is not limited to, refraining from posting offensive or inappropriate content, respecting the privacy of others, and adhering to Company policies and procedures.

Special Security Devices
Securitas USA uses special security devices, such as surveillance cameras, alarm systems, and access control systems, to protect Company property and ensure the safety of its employees and clients.
Surveillance Cameras: Surveillance cameras are used to monitor Company property and to deter criminal activity. Employees should be aware that they may be recorded while on Company property, and that the recordings may be used for investigative or disciplinary purposes.
Alarm Systems: Alarm systems are used to protect Company property and to alert employees to potential security threats. Employees should familiarize themselves with the location of alarm systems and the procedures for activating and deactivating them.
Access Control Systems: Access control systems are used to restrict access to certain areas of Company property. Employees are responsible for safeguarding their access cards or keys and for reporting any lost or stolen cards or keys to their supervisor immediately.

Technology and Computer Use
Employees are expected to use Company technology and computer systems responsibly and in accordance with Company policies and procedures. This includes using technology and computer systems for business purposes only, safeguarding Company data, and adhering to the Company's security protocols.
Use of Technology: Employees are expected to use Company technology and computer systems for business purposes only. Personal use of Company technology and computer systems should be kept to a minimum and should not interfere with work responsibilities.
Data Security: Employees are responsible for safeguarding Company data from unauthorized access, use, or disclosure. This includes using strong passwords, following Company protocols for data protection, and reporting any security breaches to their supervisor immediately.
Software and Hardware: Employees are not permitted to install or download software or hardware on Company computers or devices without prior approval from their supervisor or the IT Department. Unauthorized software or hardware may pose a security risk and may result in disciplinary action, up to and including termination of employment.

Telecommuting and Remote Work
Securitas USA may allow employees to telecommute or work remotely under certain circumstances. Telecommuting and remote work arrangements are subject to Company policies and procedures and must be approved by the employee's supervisor and Human Resources representative.
Eligibility: Employees who wish to telecommute or work remotely must meet certain eligibility requirements, including having a job that can be performed remotely, having the necessary technology and equipment, and having a suitable workspace.
Approval: Employees who wish to telecommute or work remotely must obtain approval from their supervisor and Human Resources representative. Telecommuting and remote work arrangements may be temporary or permanent, depending on the needs of the Company and the employee.
Responsibilities: Employees who telecommute or work remotely are expected to maintain the same level of productivity and professionalism as they would in the office. This includes adhering to their work schedule, staying in communication with their supervisor and coworkers, and following Company policies and procedures.

Termination of Employment
Termination of employment may occur for various reasons, including voluntary resignation, involuntary separation, or retirement. Employees are expected to follow the Company's procedures for terminating their employment, including returning Company property and providing notice of resignation.
Voluntary Separation: A separation is considered voluntary when you elect to resign. Whenever possible, you are requested to submit, in writing, the reason for resignation and your anticipated departure date.
Final Wages: Your final paycheck will be provided to you as required by applicable state law.
Life Insurance Portability/Conversion: Separated employees covered by Securitas USA’s Group Term Life Insurance will be provided with notices regarding options to continue or convert their term life insurance coverage. Appropriate paperwork must be signed and submitted to the Insurance Carrier directly within 30 days of employment termination. If you are interested in continuing or converting your life insurance, you should contact the WOC Benefits Department.

Timekeeping and Off-the-Clock Work
Employees are responsible for accurately recording their work hours and for adhering to Company policies regarding timekeeping and off-the-clock work.
Timekeeping: Employees are required to accurately record their work hours using the Company's timekeeping system. This includes recording the start and end of each workday, as well as any breaks or meal periods. Employees are prohibited from altering or falsifying their time records.
Off-the-Clock Work: Employees are not permitted to work off-the-clock or to perform work-related tasks outside of their scheduled work hours without prior approval from their supervisor. This includes but is not limited to, checking email, responding to phone calls, or completing work assignments outside of scheduled work hours.

Training and Development
Securitas USA is committed to providing employees with the training and development opportunities they need to succeed in their roles. Employees are expected to participate in Company-sponsored training and development programs and to take advantage of opportunities for professional growth.
Training Programs: Securitas USA offers a variety of training programs to help employees develop the skills and knowledge they need to succeed in their roles. These programs may include on-the-job training, classroom training, online training, and other forms of instruction.
Professional Development: Employees are encouraged to take advantage of opportunities for professional development, including attending conferences, workshops, and seminars, pursuing advanced degrees or certifications, and participating in industry associations or professional organizations.
Performance Reviews: Employees will receive regular performance reviews to assess their progress and identify areas for improvement. Performance reviews may be conducted annually, semi-annually, or as needed, depending on the employee's role and performance.

Vehicle Management
Securitas USA provides vehicles to employees for use in the performance of their job duties. Employees are expected to use Company vehicles responsibly and in accordance with Company policies and procedures.
Vehicle Use: Employees are expected to use Company vehicles for business purposes only. Personal use of Company vehicles is prohibited without prior approval from the employee's supervisor. Employees are responsible for maintaining Company vehicles in good condition and for reporting any damage or mechanical issues to their supervisor immediately.
Vehicle Safety: Employees are expected to follow all Company policies and procedures regarding vehicle safety, including wearing seat belts, obeying traffic laws, and refraining from using electronic devices while driving. Employees who are involved in a vehicle accident while driving a Company vehicle must report the incident to their supervisor immediately.
Fuel and Maintenance: Employees are responsible for refueling Company vehicles as needed and for ensuring that vehicles are properly maintained. Employees should follow the Company's guidelines for vehicle maintenance and should report any maintenance issues to their supervisor immediately.

Vehicle Use and Safety
Employees who are required to drive as part of their job duties are expected to follow all Company policies and procedures regarding vehicle use and safety.
Driver's License: Employees who are required to drive as part of their job duties must maintain a valid driver's license and a clean driving record. Employees who lose their driver's license or who are involved in a traffic violation must report the incident to their supervisor immediately.
Vehicle Safety: Employees are expected to follow all Company policies and procedures regarding vehicle safety, including wearing seat belts, obeying traffic laws, and refraining from using electronic devices while driving. Employees who are involved in a vehicle accident while driving a Company vehicle must report the incident to their supervisor immediately.
Vehicle Maintenance: Employees who are assigned a Company vehicle are responsible for ensuring that the vehicle is properly maintained. This includes following the Company's guidelines for vehicle maintenance, refueling the vehicle as needed, and reporting any mechanical issues to their supervisor immediately.

Viega Company Manager/Supervisor Roster
Viega Company Manager/Supervisor Roster - This section includes the names and contact information of the key managers and supervisors at Viega. It is crucial for communication and reporting purposes.
Securitas Company Roster - This section includes the names and contact information of the key managers and supervisors at Securitas. This section is essential for internal communication.

Voluntary Separation
A separation is considered voluntary when you elect to resign. Whenever possible, you are requested to submit, in writing, the reason for resignation and your anticipated departure date.
If you are thinking of resigning, please talk it over with your supervisor and/or your branch management before doing so. If you do decide to leave, we would appreciate two weeks’ notice, although this is not required. Employees who provide adequate amount of notice will be considered to have resigned in good standing and generally will be eligible for rehire.
If you fail to report for work after three (3) consecutive workdays without contacting your supervisor, or fail to return from a leave of absence on the designated date, you may be considered to have voluntarily terminated your employment with Securitas USA.

Workers' Compensation
Securitas USA has Workers’ Compensation insurance coverage, as required by law, to protect employees who are injured on the job. This insurance provides medical, surgical, and hospital treatment in addition to payment for loss of earnings that result from work-related injuries. The cost of this coverage is paid by Securitas USA.
Reporting Injuries: If you are injured while working, you must report the incident to your supervisor within a reasonable period of time, proportionate to the seriousness of the injury or illness, regardless of how minor the injury or illness may be. If you have any questions regarding the Workers’ Compensation Insurance Program, please contact your branch office.

Workplace Violence
Securitas USA is committed to providing a safe and secure work environment for all employees. Workplace violence, including but not limited to, physical assaults, threats of violence, intimidation, and harassment, is strictly prohibited.
Prohibited Conduct: Workplace violence includes but is not limited to, physical assaults, threats of violence, intimidation, and harassment. This includes behavior that occurs on Company property, during work hours, or while on duty. Employees who engage in workplace violence may be subject to disciplinary action, up to and including termination of employment.
Reporting Incidents: Employees who experience or witness workplace violence should report the incident to their supervisor, Human Resources representative, or the Company's Ethics Hotline immediately. The Company will investigate all reports of workplace violence and will take appropriate corrective action if necessary.
Preventive Measures: The Company is committed to preventing workplace violence and will take appropriate measures to ensure the safety and security of its employees. This may include providing training on workplace violence prevention, conducting risk assessments, and implementing security measures.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": sop_context},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5
        )
        answer = response['choices'][0]['message']['content'].strip()
        return jsonify({'answer': answer})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'answer': 'An error occurred.'})

if __name__ == '__main__':
    app.run(debug=True)