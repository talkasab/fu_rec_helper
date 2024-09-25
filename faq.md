### Why are we launching this program? Where did this program come from?

- Diagnostic errors (missed or delayed diagnoses) are a leading cause of patient
  harm, in the United States, including at MGB. Failing to perform clinically necessary
  testing in a timely fashion, including follow up imaging, is a major contributing factor
  to diagnostic error.
- Approximately 10% of radiology reports contain at least one recommendation for
  follow up imaging, and there is substantial variation among radiologists in the rates
  and language used to make recommendations.
- _Clinically Significant Result (CSR)-Action_ is a unique, best-in-class  **MGB designed system of care** that
  uses the Electronic Health Record and incorporates the policies, functions, and
  workflows of a successful program used at BWH over the past 5 years (known as
  Addressing Radiologist Recommendations Collaboratively or ARRC). CSR-Action
  helps ensure timely performance of clinically necessary radiologists’ follow up
  recommendations. The CSR program is overseen by the MGB Office of CMO and is
  being implemented across all MGB sites in FY24.
- CSR-Action involves 3 broad steps:
  - The radiologist makes an Actionable
  Recommendation (one that explicitly communicates the rationale, modality, body
  region, and time range);
  - A responsible provider explicitly agrees/disagrees with each
  discrete recommendation; and 
  - safetynet/care coordination teams help ensure that
  recommendations that were agreed upon are tracked to timely completion to prevent
  patient harm.

### Will PowerScribe (PS) force me to submit an actionable recommendation for CSR-Action when I am dictating a report?

**No.** You choose when to launch the follow up recommendation tool in Powerscribe
(PS) before you finalize the report to create an actionable recommendation.
However, without an actionable recommendation, the patient and providers will not
benefit from the CSR-Action system of care.

:material/link: [Basic Usage](/basic_usage)

### Will PS automatically insert the documentation of communication of follow up at the bottom of my report like it does for CSR-Acknowledge?

**No.** You should insert it yourself. Dictation does not work after invoking the follow up
tool. Either:

- Insert via voice command “Macro: Documented” before invoking the tool; or 
- Use "Insert > Autotext" (works fine after tool is used).

### Why am I being asked to addend my report with this program? I was not being asked to create addendums for this program before (relevant to BWPO users)

Because the new program is integrated into PowerScribe, you will need to addend the report if you are creating a new actionable recommendation. **You will be asked to addend your report and create a new actionable recommendation for additional diagnostic radiology exams as soon as possible** if:

- The recommendation you create does not have ALL the elements needed to be actionable (time range, modality, body part and rationale for follow up). This may happen because the new follow up tool does not require you to enter the needed elements (we are actively working with the vendor to address this), and therefore you may miss entering some of the elements unless you scrutinize each element. The resultant *incomplete* recommendation will be submitted to Epic. You will then receive an email to addend the report so that your recommendation is complete and that an actionable recommendation is submitted to Epic replacing the incomplete recommendation.
- If the ‘Begin’ and ‘End’ time times are the same (or less than 2 weeks).
- If you erroneously click ‘Flag for review button’ (*we are actively working with the vendor to remove/hide this button that should NEVER be clicked in our workflow*).
- You will not be asked to addend recommendations for referrals (i.e., consults) or procedures (e.g., endoscopy, tissue sampling). These recommendations do not require a timeframe as access to other physician services are not overseen by CSR-Action. An Ambulatory SafetyNet team (overseen by OCMO) will still track agreed upon recommendations to completion.

### Do I have to use the recommendation macro?

**No.** The use of the macro is at your discretion. If you do, it will guide you or your trainee to tab through each actionable recommendation required element (you can navigate through the same fields which are visible on the follow up window in PS once you launch it). If you use the macro, you should still scrutinize ALL elements of each recommendation in the follow up window. You should be aware that the text in the macro may be redundant with some of the information you typically dictate in your impression.

### Do I need to dictate all the required elements of an actionable recommendation in my text report?

**No.** All elements are required ONLY in the follow up window. For example, you may dictate ‘Chest CT in 6 months’, but you will also need to choose an appropriate time range (the tool will erroneously map ‘in 6 months’ to Begin/End times of 180 days-180 days which you need to correct with a clinically-appropriate time range for the patient).

### Can I ask my trainee to create the follow up recommendation in the follow up tool?

**No.** While trainees can generate CSR-Acknowledge alerts, they are not given access to use the follow up tool. You may consider asking trainees to use the recommendation macro as described above.

:material/link: [Trainee Workflow](/trainee_workflow)

### How short can the timeframe range be?

The tool allows you to choose whatever time-range you choose. However, the time range should reflect your clinical judgment about how soon it is appropriate to get the follow up (i.e., Begin time) and beyond what timeframe the follow up would no longer be appropriate (i.e., End time). As clinically appropriate, the longer the time range, the easier it is to schedule the patient’s follow up. Time ranges shorter than 2 weeks are exceeding challenging to coordinate for the hundreds of referring provider offices across MGB which use this time range to book an imaging exam consistent with patient preference for time & location, often coordinating with an ordering provider appointment.

> Follow up recommendations needed to prevent potential patient
> harm within 2 weeks are best communicated using the appropriate
> CSR acknowledge alert.

### Should I generate follow up recommendations for inpatient and ED patients if follow up should happen while they are inpatients or in the ED?

**No.** Please use the appropriate CSR-Acknowledge workflow.

You should generate follow up recommendation using the follow up tool if the follow up should or can be appropriately performed as an outpatient.

### How do I know my recommendation was submitted to Epic?

The [Recommendation Dashboard](https://csrraddash.partners.org) shows your recommendation approximately 2–5 minutes after final signing (MGB network only).

In addition, you can see your recommendation as providers see it at the top of the report when viewed in Epic. It may take up to 5 min for recommendation to appear with the result in Epic.

### Can I see/track my recommendations to keep track of them?

**Yes.** The [Recommendation Dashboard](https://csrraddash.partners.org) shows your recommendations (MGB network only).

:material/info: [Dashboard Info](/dashboard)

### Will I receive reports showing my recommendations rates compare to my MGB peers?

**Yes.** The first such report will be distributed at the end of October, then monthly. These are currently organized by subspecialty/Division.

### If I have feedback about the program how/who do I submit it?

If you have technical issues, please submit a ticket to the MI2 Service Desk (<mi2isd@partners.org>).

If you have program feedback, you can:

- Submit email to the CSR Admin team (<CSRadmin@mgb.org>)
- Send CSR feedback in Worth Another Look
- Email Ramin Khorasani (<rkhorasani@bwh.harvard.edu>) or Patrick Curley (<pcurley@mgb.org>)

### If I make a mistake and send the wrong recommendation, what should I do?

Please create a new actionable recommendation (if you have already signed your report you will need to addend it) and send email to MGB Radiology Safetynet team (<safetynet@bwh.harvard.edu>)

### If the tool creates multiple recommendations for a single recommendation in my report, can I just accept one and sign?

**No.** Unless you accept/decline each recommendation in the Follow up tool, none will be submitted to Epic. Canceling or closing the dialog out deletes all recommendations, including those previously accepted.

### What if I have an urgent result (diverticulitis) and a separate finding needing follow up (pulmonary nodule)?

**Sent two alerts:** a CSR acknowledge urgent alert, and a separate actionable recommendation for pulmonary nodule follow up.

### Do I need to send Important check Epic and a follow up recommendation if I have an important finding that also needs follow up (unexpected new liver lesion)?

**No.** you only need to create an actionable recommendation for follow up. Responsible provider's response to the actionable recommendation will also 'acknowledge' the important result. There is no no need to also send a separate CSR Acknowledge alert.

### What should I do If I think two modalities will be equally appropriate for a recommendation?

Select the one you prefer, then add the alternate modality in the additional text field of the follow up tool.

### Will trainees see the rationale for recommendation I enter in the follow up tool when they protocol the follow up exam?

**Yes.** The rationale will be available in the protocolling workflow in Epic.
