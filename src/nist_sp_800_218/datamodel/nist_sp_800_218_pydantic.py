from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "1.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'cprt_framework_version': {'tag': 'cprt_framework_version',
                                                'value': 'SP_800_218_1_1_0'},
                     'oscal_content_commit': {'tag': 'oscal_content_commit',
                                              'value': 'f0de6d8d8c059d374f15e0ae07508d82e370fc1d'},
                     'oscal_content_tag': {'tag': 'oscal_content_tag',
                                           'value': 'v1.6.0'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2022-02'}},
     'comments': ['The version is the SSDF version that SP 800-218 defines, and '
                  "source is the publication's digital object identifier. NIST's "
                  'Cybersecurity and Privacy Reference Tool names the same version '
                  'SP_800_218_1_1_0, and the catalog NIST publishes for it in '
                  'usnistgov/oscal-content is copied to '
                  'src/nist_sp_800_218/schema/oscal-content/ at the tag and commit '
                  'in the annotations. scripts/check_upstream_release.py reads the '
                  'same pins and reports when NIST publishes a newer edition or '
                  "changes the catalog. The release tags are the schema's own "
                  'versions.',
                  'SP 800-218 is a work of the United States Government and is not '
                  'subject to copyright in the United States. The descriptions '
                  "here are this project's own words; NIST's text of each "
                  'practice, task and example stays in the catalog copy.',
                  "NIST's catalog renders each practice group as an OSCAL group, "
                  'each practice and task as an OSCAL control, each example as a '
                  'part and each reference as a link. The broad_mappings name '
                  'those lmodel/oscal classes.'],
     'default_prefix': 'nist_sp_800_218',
     'default_range': 'string',
     'description': 'A LinkML model of the Secure Software Development Framework '
                    '(SSDF) version 1.1, which NIST Special Publication 800-218 '
                    'recommends: its practice groups, practices and tasks, the '
                    'notional implementation examples of each task, and the '
                    'references that map each task to other secure software '
                    'development documents.',
     'id': 'https://w3id.org/lmodel/nist-sp-800-218',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist_sp_800_218',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_218': {'prefix_prefix': 'nist_sp_800_218',
                                      'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-218/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/nist-sp-800-218',
                  'https://csrc.nist.gov/pubs/sp/800/218/final',
                  'https://csrc.nist.gov/projects/ssdf',
                  'https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/SP800-218/ver1'],
     'source': 'https://doi.org/10.6028/NIST.SP.800-218',
     'source_file': 'src/nist_sp_800_218/schema/nist_sp_800_218.yaml',
     'title': 'Secure Software Development Framework (SSDF) version 1.1',
     'types': {'ssdf_example_identifier': {'base': 'str',
                                           'description': "The identifier NIST's "
                                                          'reference data gives a '
                                                          'notional implementation '
                                                          "example: its task's "
                                                          'identifier, a dot and '
                                                          "the example's number, "
                                                          'such as PO.1.1.1.',
                                           'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
                                           'name': 'ssdf_example_identifier',
                                           'pattern': '^(PO|PS|PW|RV)\\.[1-9][0-9]*\\.[1-9][0-9]*\\.[1-9][0-9]*$',
                                           'typeof': 'string',
                                           'uri': 'xsd:string'},
               'ssdf_group_identifier': {'base': 'str',
                                         'description': 'The two letters that name '
                                                        'one of the four practice '
                                                        'groups.',
                                         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
                                         'name': 'ssdf_group_identifier',
                                         'pattern': '^(PO|PS|PW|RV)$',
                                         'typeof': 'string',
                                         'uri': 'xsd:string'},
               'ssdf_practice_identifier': {'base': 'str',
                                            'description': "A practice's "
                                                           'identifier: its '
                                                           "group's letters, a dot "
                                                           "and the practice's "
                                                           'number within the '
                                                           'group, such as PO.1.',
                                            'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
                                            'name': 'ssdf_practice_identifier',
                                            'pattern': '^(PO|PS|PW|RV)\\.[1-9][0-9]*$',
                                            'typeof': 'string',
                                            'uri': 'xsd:string'},
               'ssdf_task_identifier': {'base': 'str',
                                        'description': "A task's identifier: its "
                                                       "practice's identifier, a "
                                                       "dot and the task's number "
                                                       'within the practice, such '
                                                       'as PO.1.1.',
                                        'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
                                        'name': 'ssdf_task_identifier',
                                        'pattern': '^(PO|PS|PW|RV)\\.[1-9][0-9]*\\.[1-9][0-9]*$',
                                        'typeof': 'string',
                                        'uri': 'xsd:string'}}} )

class SsdfReferenceDocument(str, Enum):
    """
    The established secure development documents that SP 800-218 maps its tasks to, by the labels its References list gives them. SP 800-218 cites each at the edition shown in its title.
    """
    The_BSA_Framework_for_Secure_Software_version_1FULL_STOP1_LEFT_PARENTHESIS2020RIGHT_PARENTHESIS = "BSAFSS"
    """
    BSA's framework for securing the software lifecycle.
    """
    BSIMM12_2021_Foundations_Report = "BSIMM"
    """
    The Building Security In Maturity Model, twelfth edition.
    """
    Software_Supply_Chain_Best_Practices_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "CNCFSSCP"
    """
    The Cloud Native Computing Foundation's software supply chain paper.
    """
    Executive_Order_14028_Improving_the_NationAPOSTROPHEs_Cybersecurity_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "EO14028"
    """
    The executive order whose Section 4e clauses SP 800-218 maps in its Appendix A.
    """
    State_of_the_Art_Resources_LEFT_PARENTHESISSOARRIGHT_PARENTHESIS_for_Software_Vulnerability_Detection_Test_and_Evaluation_2016 = "IDASOAR"
    """
    The Institute for Defense Analyses report on software vulnerability tools and techniques.
    """
    IEC_62443_4_1COLON2018_Secure_product_development_lifecycle_requirements = "IEC62443"
    """
    The International Electrotechnical Commission's standard for secure development of industrial automation and control products.
    """
    NIST_IR_8397_Guidelines_on_Minimum_Standards_for_Developer_Verification_of_Software_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "IR8397"
    """
    NIST's guidelines for the verification a software developer performs.
    """
    ISOSOLIDUSIEC_27034_1COLON2011_Application_security_Part_1 = "ISO27034"
    """
    The international standard's overview and concepts of application security.
    """
    ISOSOLIDUSIEC_29147COLON2018_Vulnerability_disclosure = "ISO29147"
    """
    The international standard for disclosing vulnerabilities in products and services.
    """
    ISOSOLIDUSIEC_30111COLON2019_Vulnerability_handling_processes = "ISO30111"
    """
    The international standard for the processes that handle a reported vulnerability.
    """
    Microsoft_Security_Development_Lifecycle_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "MSSDL"
    """
    Microsoft's practices for building security into software development.
    """
    Framework_for_Improving_Critical_Infrastructure_Cybersecurity_version_1FULL_STOP1_LEFT_PARENTHESIS2018RIGHT_PARENTHESIS = "NISTCSF"
    """
    The NIST Cybersecurity Framework at version 1.1, which SP 800-218 maps to by subcategory.
    """
    Recommended_Criteria_for_Cybersecurity_Labeling_of_Consumer_Software_LEFT_PARENTHESIS2022RIGHT_PARENTHESIS = "NISTLABEL"
    """
    NIST's criteria for a cybersecurity label on consumer software.
    """
    The_Minimum_Elements_For_a_Software_Bill_of_Materials_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "NTIASBOM"
    """
    The National Telecommunications and Information Administration's minimum elements of a software bill of materials.
    """
    OWASP_Application_Security_Verification_Standard_4FULL_STOP0FULL_STOP3_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "OWASPASVS"
    """
    The Open Web Application Security Project's verification standard for applications.
    """
    OWASP_Mobile_Application_Security_Verification_Standard_version_1FULL_STOP4FULL_STOP2_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "OWASPMASVS"
    """
    The Open Web Application Security Project's verification standard for mobile applications.
    """
    Software_Assurance_Maturity_Model_version_1FULL_STOP5_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "OWASPSAMM"
    """
    The Open Web Application Security Project's software assurance maturity model.
    """
    OWASP_Software_Component_Verification_Standard_version_1FULL_STOP0_LEFT_PARENTHESIS2020RIGHT_PARENTHESIS = "OWASPSCVS"
    """
    The Open Web Application Security Project's verification standard for software components.
    """
    Secure_Software_Lifecycle_LEFT_PARENTHESISSecure_SLCRIGHT_PARENTHESIS_Requirements_and_Assessment_Procedures_version_1FULL_STOP1_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "PCISSLC"
    """
    The Payment Card Industry Security Standards Council's requirements for a secure software lifecycle.
    """
    Practical_Security_Stories_and_Security_Tasks_for_Agile_Development_Environments_LEFT_PARENTHESIS2012RIGHT_PARENTHESIS = "SCAGILE"
    """
    SAFECode's security stories and tasks for agile teams.
    """
    Fundamental_Practices_for_Secure_Software_Development_third_edition_LEFT_PARENTHESIS2018RIGHT_PARENTHESIS = "SCFPSSD"
    """
    SAFECode's essential elements of a secure development lifecycle program.
    """
    Software_Integrity_ControlsCOLON_An_Assurance_Based_Approach_to_Minimizing_Risks_in_the_Software_Supply_Chain_LEFT_PARENTHESIS2010RIGHT_PARENTHESIS = "SCSIC"
    """
    SAFECode's controls for software integrity in the supply chain.
    """
    Managing_Security_Risks_Inherent_in_the_Use_of_Third_Party_Components_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "SCTPC"
    """
    SAFECode's guidance on the security risks of third-party components.
    """
    Tactical_Threat_Modeling_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "SCTTM"
    """
    SAFECode's guidance on threat modeling during development.
    """
    NIST_SP_800_160_Volume_1_Systems_Security_Engineering_LEFT_PARENTHESIS2016_updated_2018RIGHT_PARENTHESIS = "SP800160"
    """
    NIST's considerations for engineering trustworthy secure systems.
    """
    NIST_SP_800_161_RevFULL_STOP_1_second_draft_Cybersecurity_Supply_Chain_Risk_Management_Practices_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "SP800161"
    """
    NIST's supply chain risk management practices, at the draft SP 800-218 cites.
    """
    NIST_SP_800_181_NICE_Cybersecurity_Workforce_Framework_LEFT_PARENTHESIS2017RIGHT_PARENTHESIS = "SP800181"
    """
    The workforce framework whose tasks, knowledge, skills and abilities SP 800-218 maps to.
    """
    NIST_SP_800_216_draft_Recommendations_for_Federal_Vulnerability_Disclosure_Guidelines_LEFT_PARENTHESIS2021RIGHT_PARENTHESIS = "SP800216"
    """
    NIST's recommendations for federal vulnerability disclosure, at the draft SP 800-218 cites.
    """
    NIST_SP_800_53_RevFULL_STOP_5_Security_and_Privacy_Controls_for_Information_Systems_and_Organizations_LEFT_PARENTHESIS2020RIGHT_PARENTHESIS = "SP80053"
    """
    NIST's catalog of security and privacy controls, which SP 800-218 maps to by control.
    """



class SsdfFramework(ConfiguredBaseModel):
    """
    One version of the SSDF as a whole: its practice groups, each holding its practices and their tasks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_sp_800_218:Framework',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/218/final'],
         'tree_root': True})

    ssdf_version: str = Field(default=..., description="""The SSDF version, as NIST numbers it in the publication's title, such as 1.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfFramework']} })
    practice_groups: list[SsdfPracticeGroup] = Field(default=..., description="""The practice groups, in the order SP 800-218 gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfFramework']} })

    @field_validator('ssdf_version')
    def pattern_ssdf_version(cls, v):
        pattern=re.compile(r"^[0-9]+\.[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid ssdf_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid ssdf_version format: {v}"
            raise ValueError(err_msg)
        return v


class SsdfPracticeGroup(ConfiguredBaseModel):
    """
    One of the four groups SP 800-218 sorts its practices into: preparing the organization, protecting the software, producing well-secured software, and responding to vulnerabilities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Group'],
         'class_uri': 'nist_sp_800_218:PracticeGroup',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'see_also': ['https://csrc.nist.gov/projects/ssdf']})

    title: Optional[str] = Field(default=None, description="""The name SP 800-218 gives the practice group or practice.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['SsdfPracticeGroup', 'SsdfPractice'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the practice group, practice, task or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['SsdfPracticeGroup',
                       'SsdfPractice',
                       'SsdfTask',
                       'SsdfImplementationExample'],
         'slot_uri': 'schema:description'} })
    group_id: str = Field(default=..., description="""The group's two letters, such as PO for Prepare the Organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfPracticeGroup']} })
    group_practices: Optional[list[SsdfPractice]] = Field(default=None, description="""The practices of the group. A knowledge bundle relates a practice to its group with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfPracticeGroup']} })


class SsdfPractice(ConfiguredBaseModel):
    """
    A secure software development practice: a named outcome with an identifier, a short explanation of what it is and why it helps, and the tasks that may be needed to achieve it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_sp_800_218:Practice',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'see_also': ['https://csrc.nist.gov/projects/ssdf']})

    title: Optional[str] = Field(default=None, description="""The name SP 800-218 gives the practice group or practice.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['SsdfPracticeGroup', 'SsdfPractice'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the practice group, practice, task or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['SsdfPracticeGroup',
                       'SsdfPractice',
                       'SsdfTask',
                       'SsdfImplementationExample'],
         'slot_uri': 'schema:description'} })
    practice_id: str = Field(default=..., description="""The practice's identifier, such as PO.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfPractice']} })
    practice_tasks: Optional[list[SsdfTask]] = Field(default=None, description="""The tasks of the practice. A knowledge bundle relates a task to its practice with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfPractice']} })


class SsdfTask(ConfiguredBaseModel):
    """
    An action that may be needed to perform a practice, with notional examples of how it could be implemented and references to the documents whose practices it maps to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_sp_800_218:Task',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'see_also': ['https://csrc.nist.gov/projects/ssdf']})

    description: Optional[str] = Field(default=None, description="""What the practice group, practice, task or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['SsdfPracticeGroup',
                       'SsdfPractice',
                       'SsdfTask',
                       'SsdfImplementationExample'],
         'slot_uri': 'schema:description'} })
    task_id: str = Field(default=..., description="""The task's identifier, such as PO.1.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfTask']} })
    former_task_ids: Optional[list[str]] = Field(default=None, description="""The identifiers the task had in an earlier SSDF version, which SP 800-218 notes beside the task after moving it, such as PW.3.1 for PO.1.3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfTask']} })
    implementation_examples: Optional[list[SsdfImplementationExample]] = Field(default=None, description="""Notional examples of tools, processes or other methods that could help implement the task. SP 800-218 requires none of them and does not claim they are the only ways.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfTask']} })
    task_references: Optional[list[SsdfReference]] = Field(default=None, description="""The established secure development documents the task maps to, each with the parts of the document it maps to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfTask']} })


class SsdfImplementationExample(ConfiguredBaseModel):
    """
    A notional implementation example: one type of tool, process or other method that could help implement a task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_218:ImplementationExample',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'see_also': ['https://csrc.nist.gov/projects/ssdf'],
         'slot_usage': {'description': {'name': 'description', 'required': True}}})

    description: str = Field(default=..., description="""What the practice group, practice, task or example says, in the words of whoever records it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['SsdfPracticeGroup',
                       'SsdfPractice',
                       'SsdfTask',
                       'SsdfImplementationExample'],
         'slot_uri': 'schema:description'} })
    example_id: str = Field(default=..., description="""The example's identifier in NIST's reference data, such as PO.1.1.1 for the first example of task PO.1.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfImplementationExample']} })


class SsdfReference(ConfiguredBaseModel):
    """
    A pointer from a task to an established secure development document, and to the parts of that document the task maps to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Link'],
         'class_uri': 'nist_sp_800_218:Reference',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'see_also': ['https://csrc.nist.gov/projects/ssdf']})

    reference_document: SsdfReferenceDocument = Field(default=..., description="""The document the task maps to, by the label SP 800-218 gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfReference']} })
    mapped_items: str = Field(default=..., description="""The parts of the document the task maps to, as SP 800-218 lists them, such as the clause, control or activity identifiers SM.3, DE.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SsdfReference']} })

    @field_validator('mapped_items')
    def pattern_mapped_items(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid mapped_items format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid mapped_items format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SsdfFramework.model_rebuild()
SsdfPracticeGroup.model_rebuild()
SsdfPractice.model_rebuild()
SsdfTask.model_rebuild()
SsdfImplementationExample.model_rebuild()
SsdfReference.model_rebuild()
