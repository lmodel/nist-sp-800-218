/**
* The established secure development documents that SP 800-218 maps its tasks to, by the labels its References list gives them. SP 800-218 cites each at the edition shown in its title.
*/
export enum SsdfReferenceDocument {
    
    /** BSA's framework for securing the software lifecycle. */
    The_BSA_Framework_for_Secure_Software_version_1FULL_STOP1_LEFT_PARENTHESIS2020RIGHT_PARENTHESIS = "BSAFSS",
    /** The Building Security In Maturity Model, twelfth edition. */
    BSIMM12_2021_Foundations_Report = "BSIMM",
    /** The Cloud Native Computing Foundation's software supply chain paper. */
    Software_Supply_Chain_Best_Practices_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "CNCFSSCP",
    /** The executive order whose Section 4e clauses SP 800-218 maps in its Appendix A. */
    Executive_Order_14028_Improving_the_NationAPOSTROPHEs_Cybersecurity_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "EO14028",
    /** The Institute for Defense Analyses report on software vulnerability tools and techniques. */
    State_of_the_Art_Resources_LEFT_PARENTHESISSOARRIGHT_PARENTHESIS_for_Software_Vulnerability_Detection_Test_and_Evaluation_2016 = "IDASOAR",
    /** The International Electrotechnical Commission's standard for secure development of industrial automation and control products. */
    IEC_62443_4_1COLON2018_Secure_product_development_lifecycle_requirements = "IEC62443",
    /** NIST's guidelines for the verification a software developer performs. */
    NIST_IR_8397_Guidelines_on_Minimum_Standards_for_Developer_Verification_of_Software_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "IR8397",
    /** The international standard's overview and concepts of application security. */
    ISOSOLIDUSIEC_27034_1COLON2011_Application_security_Part_1 = "ISO27034",
    /** The international standard for disclosing vulnerabilities in products and services. */
    ISOSOLIDUSIEC_29147COLON2018_Vulnerability_disclosure = "ISO29147",
    /** The international standard for the processes that handle a reported vulnerability. */
    ISOSOLIDUSIEC_30111COLON2019_Vulnerability_handling_processes = "ISO30111",
    /** Microsoft's practices for building security into software development. */
    Microsoft_Security_Development_Lifecycle_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "MSSDL",
    /** The NIST Cybersecurity Framework at version 1.1, which SP 800-218 maps to by subcategory. */
    Framework_for_Improving_Critical_Infrastructure_Cybersecurity_version_1FULL_STOP1_LEFT_PARENTHESIS2018RIGHT_PARENTHESIS = "NISTCSF",
    /** NIST's criteria for a cybersecurity label on consumer software. */
    Recommended_Criteria_for_Cybersecurity_Labeling_of_Consumer_Software_LEFT_PARENTHESIS2022RIGHT_PARENTHESIS = "NISTLABEL",
    /** The National Telecommunications and Information Administration's minimum elements of a software bill of materials. */
    The_Minimum_Elements_For_a_Software_Bill_of_Materials_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "NTIASBOM",
    /** The Open Web Application Security Project's verification standard for applications. */
    OWASP_Application_Security_Verification_Standard_4FULL_STOP0FULL_STOP3_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "OWASPASVS",
    /** The Open Web Application Security Project's verification standard for mobile applications. */
    OWASP_Mobile_Application_Security_Verification_Standard_version_1FULL_STOP4FULL_STOP2_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "OWASPMASVS",
    /** The Open Web Application Security Project's software assurance maturity model. */
    Software_Assurance_Maturity_Model_version_1FULL_STOP5_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "OWASPSAMM",
    /** The Open Web Application Security Project's verification standard for software components. */
    OWASP_Software_Component_Verification_Standard_version_1FULL_STOP0_LEFT_PARENTHESIS2020RIGHT_PARENTHESIS = "OWASPSCVS",
    /** The Payment Card Industry Security Standards Council's requirements for a secure software lifecycle. */
    Secure_Software_Lifecycle_LEFT_PARENTHESISSecure_SLCRIGHT_PARENTHESIS_Requirements_and_Assessment_Procedures_version_1FULL_STOP1_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "PCISSLC",
    /** SAFECode's security stories and tasks for agile teams. */
    Practical_Security_Stories_and_Security_Tasks_for_Agile_Development_Environments_LEFT_PARENTHESIS2012RIGHT_PARENTHESIS = "SCAGILE",
    /** SAFECode's essential elements of a secure development lifecycle program. */
    Fundamental_Practices_for_Secure_Software_Development_third_edition_LEFT_PARENTHESIS2018RIGHT_PARENTHESIS = "SCFPSSD",
    /** SAFECode's controls for software integrity in the supply chain. */
    Software_Integrity_ControlsCOLON_An_Assurance_Based_Approach_to_Minimizing_Risks_in_the_Software_Supply_Chain_LEFT_PARENTHESIS2010RIGHT_PARENTHESIS = "SCSIC",
    /** SAFECode's guidance on the security risks of third-party components. */
    Managing_Security_Risks_Inherent_in_the_Use_of_Third_Party_Components_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "SCTPC",
    /** SAFECode's guidance on threat modeling during development. */
    Tactical_Threat_Modeling_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "SCTTM",
    /** NIST's considerations for engineering trustworthy secure systems. */
    NIST_SP_800_160_Volume_1_Systems_Security_Engineering_LEFT_PARENTHESIS2016_updated_2018RIGHT_PARENTHESIS = "SP800160",
    /** NIST's supply chain risk management practices, at the draft SP 800-218 cites. */
    NIST_SP_800_161_RevFULL_STOP_1_second_draft_Cybersecurity_Supply_Chain_Risk_Management_Practices_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "SP800161",
    /** The workforce framework whose tasks, knowledge, skills and abilities SP 800-218 maps to. */
    NIST_SP_800_181_NICE_Cybersecurity_Workforce_Framework_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "SP800181",
    /** NIST's recommendations for federal vulnerability disclosure, at the draft SP 800-218 cites. */
    NIST_SP_800_216_draft_Recommendations_for_Federal_Vulnerability_Disclosure_Guidelines_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "SP800216",
    /** NIST's catalog of security and privacy controls, which SP 800-218 maps to by control. */
    NIST_SP_800_53_RevFULL_STOP_5_Security_and_Privacy_Controls_for_Information_Systems_and_Organizations_LEFT_PARENTHESIS2020RIGHT_PARENTHESIS = "SP80053",
};


/**
 * One version of the SSDF as a whole: its practice groups, each holding its practices and their tasks.
 */
export interface SsdfFramework {
    /** The SSDF version, as NIST numbers it in the publication's title, such as 1.1. */
    ssdf_version: string,
    /** The practice groups, in the order SP 800-218 gives them. */
    practice_groups: SsdfPracticeGroup[],
}


/**
 * One of the four groups SP 800-218 sorts its practices into: preparing the organization, protecting the software, producing well-secured software, and responding to vulnerabilities.
 */
export interface SsdfPracticeGroup {
    /** The name SP 800-218 gives the practice group or practice. */
    title?: string,
    /** What the practice group, practice, task or example says, in the words of whoever records it. */
    description?: string,
    /** The group's two letters, such as PO for Prepare the Organization. */
    group_id: string,
    /** The practices of the group. A knowledge bundle relates a practice to its group with isPartOf instead. */
    group_practices?: SsdfPractice[],
}


/**
 * A secure software development practice: a named outcome with an identifier, a short explanation of what it is and why it helps, and the tasks that may be needed to achieve it.
 */
export interface SsdfPractice {
    /** The name SP 800-218 gives the practice group or practice. */
    title?: string,
    /** What the practice group, practice, task or example says, in the words of whoever records it. */
    description?: string,
    /** The practice's identifier, such as PO.1. */
    practice_id: string,
    /** The tasks of the practice. A knowledge bundle relates a task to its practice with isPartOf instead. */
    practice_tasks?: SsdfTask[],
}


/**
 * An action that may be needed to perform a practice, with notional examples of how it could be implemented and references to the documents whose practices it maps to.
 */
export interface SsdfTask {
    /** What the practice group, practice, task or example says, in the words of whoever records it. */
    description?: string,
    /** The task's identifier, such as PO.1.1. */
    task_id: string,
    /** The identifiers the task had in an earlier SSDF version, which SP 800-218 notes beside the task after moving it, such as PW.3.1 for PO.1.3. */
    former_task_ids?: string[],
    /** Notional examples of tools, processes or other methods that could help implement the task. SP 800-218 requires none of them and does not claim they are the only ways. */
    implementation_examples?: SsdfImplementationExample[],
    /** The established secure development documents the task maps to, each with the parts of the document it maps to. */
    task_references?: SsdfReference[],
}


/**
 * A notional implementation example: one type of tool, process or other method that could help implement a task.
 */
export interface SsdfImplementationExample {
    /** What the practice group, practice, task or example says, in the words of whoever records it. */
    description: string,
    /** The example's identifier in NIST's reference data, such as PO.1.1.1 for the first example of task PO.1.1. */
    example_id: string,
}


/**
 * A pointer from a task to an established secure development document, and to the parts of that document the task maps to.
 */
export interface SsdfReference {
    /** The document the task maps to, by the label SP 800-218 gives it. */
    reference_document: string,
    /** The parts of the document the task maps to, as SP 800-218 lists them, such as the clause, control or activity identifiers SM.3, DE.1. */
    mapped_items: string,
}



