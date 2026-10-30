# Auto generated from nist_sp_800_218.yaml by pythongen.py version: 0.0.1
# Schema: nist_sp_800_218
#
# id: https://w3id.org/lmodel/nist-sp-800-218
# description: A LinkML model of the Secure Software Development Framework (SSDF) version 1.1, which NIST Special Publication 800-218 recommends: its practice groups, practices and tasks, the notional implementation examples of each task, and the references that map each task to other secure software development documents.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.12.0"
version = "1.1.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_218 = CurieNamespace('nist_sp_800_218', 'https://w3id.org/lmodel/nist-sp-800-218/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_SP_800_218


# Types
class SsdfGroupIdentifier(String):
    """ The two letters that name one of the four practice groups. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ssdf_group_identifier"
    type_model_uri = NIST_SP_800_218.SsdfGroupIdentifier


class SsdfPracticeIdentifier(String):
    """ A practice's identifier: its group's letters, a dot and the practice's number within the group, such as PO.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ssdf_practice_identifier"
    type_model_uri = NIST_SP_800_218.SsdfPracticeIdentifier


class SsdfTaskIdentifier(String):
    """ A task's identifier: its practice's identifier, a dot and the task's number within the practice, such as PO.1.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ssdf_task_identifier"
    type_model_uri = NIST_SP_800_218.SsdfTaskIdentifier


class SsdfExampleIdentifier(String):
    """ The identifier NIST's reference data gives a notional implementation example: its task's identifier, a dot and the example's number, such as PO.1.1.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ssdf_example_identifier"
    type_model_uri = NIST_SP_800_218.SsdfExampleIdentifier


# Class references



@dataclass(repr=False)
class SsdfFramework(YAMLRoot):
    """
    One version of the SSDF as a whole: its practice groups, each holding its practices and their tasks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Framework"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Framework"
    class_name: ClassVar[str] = "SsdfFramework"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.SsdfFramework

    ssdf_version: str = None
    practice_groups: Union[Union[dict, "SsdfPracticeGroup"], list[Union[dict, "SsdfPracticeGroup"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ssdf_version):
            self.MissingRequiredField("ssdf_version")
        if not isinstance(self.ssdf_version, str):
            self.ssdf_version = str(self.ssdf_version)

        if self._is_empty(self.practice_groups):
            self.MissingRequiredField("practice_groups")
        self._normalize_inlined_as_list(slot_name="practice_groups", slot_type=SsdfPracticeGroup, key_name="group_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SsdfPracticeGroup(YAMLRoot):
    """
    One of the four groups SP 800-218 sorts its practices into: preparing the organization, protecting the software,
    producing well-secured software, and responding to vulnerabilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["PracticeGroup"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:PracticeGroup"
    class_name: ClassVar[str] = "SsdfPracticeGroup"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.SsdfPracticeGroup

    group_id: Union[str, SsdfGroupIdentifier] = None
    title: Optional[str] = None
    description: Optional[str] = None
    group_practices: Optional[Union[Union[dict, "SsdfPractice"], list[Union[dict, "SsdfPractice"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.group_id):
            self.MissingRequiredField("group_id")
        if not isinstance(self.group_id, SsdfGroupIdentifier):
            self.group_id = SsdfGroupIdentifier(self.group_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="group_practices", slot_type=SsdfPractice, key_name="practice_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SsdfPractice(YAMLRoot):
    """
    A secure software development practice: a named outcome with an identifier, a short explanation of what it is and
    why it helps, and the tasks that may be needed to achieve it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Practice"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Practice"
    class_name: ClassVar[str] = "SsdfPractice"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.SsdfPractice

    practice_id: Union[str, SsdfPracticeIdentifier] = None
    title: Optional[str] = None
    description: Optional[str] = None
    practice_tasks: Optional[Union[Union[dict, "SsdfTask"], list[Union[dict, "SsdfTask"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.practice_id):
            self.MissingRequiredField("practice_id")
        if not isinstance(self.practice_id, SsdfPracticeIdentifier):
            self.practice_id = SsdfPracticeIdentifier(self.practice_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="practice_tasks", slot_type=SsdfTask, key_name="task_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SsdfTask(YAMLRoot):
    """
    An action that may be needed to perform a practice, with notional examples of how it could be implemented and
    references to the documents whose practices it maps to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Task"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Task"
    class_name: ClassVar[str] = "SsdfTask"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.SsdfTask

    task_id: Union[str, SsdfTaskIdentifier] = None
    description: Optional[str] = None
    former_task_ids: Optional[Union[Union[str, SsdfTaskIdentifier], list[Union[str, SsdfTaskIdentifier]]]] = empty_list()
    implementation_examples: Optional[Union[Union[dict, "SsdfImplementationExample"], list[Union[dict, "SsdfImplementationExample"]]]] = empty_list()
    task_references: Optional[Union[Union[dict, "SsdfReference"], list[Union[dict, "SsdfReference"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task_id):
            self.MissingRequiredField("task_id")
        if not isinstance(self.task_id, SsdfTaskIdentifier):
            self.task_id = SsdfTaskIdentifier(self.task_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.former_task_ids, list):
            self.former_task_ids = [self.former_task_ids] if self.former_task_ids is not None else []
        self.former_task_ids = [v if isinstance(v, SsdfTaskIdentifier) else SsdfTaskIdentifier(v) for v in self.former_task_ids]

        self._normalize_inlined_as_list(slot_name="implementation_examples", slot_type=SsdfImplementationExample, key_name="description", keyed=False)

        self._normalize_inlined_as_list(slot_name="task_references", slot_type=SsdfReference, key_name="reference_document", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SsdfImplementationExample(YAMLRoot):
    """
    A notional implementation example: one type of tool, process or other method that could help implement a task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["ImplementationExample"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:ImplementationExample"
    class_name: ClassVar[str] = "SsdfImplementationExample"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.SsdfImplementationExample

    description: str = None
    example_id: Union[str, SsdfExampleIdentifier] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.example_id):
            self.MissingRequiredField("example_id")
        if not isinstance(self.example_id, SsdfExampleIdentifier):
            self.example_id = SsdfExampleIdentifier(self.example_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SsdfReference(YAMLRoot):
    """
    A pointer from a task to an established secure development document, and to the parts of that document the task
    maps to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Reference"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Reference"
    class_name: ClassVar[str] = "SsdfReference"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.SsdfReference

    reference_document: Union[str, "SsdfReferenceDocument"] = None
    mapped_items: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_document):
            self.MissingRequiredField("reference_document")
        if not isinstance(self.reference_document, SsdfReferenceDocument):
            self.reference_document = SsdfReferenceDocument(self.reference_document)

        if self._is_empty(self.mapped_items):
            self.MissingRequiredField("mapped_items")
        if not isinstance(self.mapped_items, str):
            self.mapped_items = str(self.mapped_items)

        super().__post_init__(**kwargs)


# Enumerations
class SsdfReferenceDocument(EnumDefinitionImpl):
    """
    The established secure development documents that SP 800-218 maps its tasks to, by the labels its References list
    gives them. SP 800-218 cites each at the edition shown in its title.
    """
    BSAFSS = PermissibleValue(
        text="BSAFSS",
        title="The BSA Framework for Secure Software, version 1.1 (2020)",
        description="BSA's framework for securing the software lifecycle.")
    BSIMM = PermissibleValue(
        text="BSIMM",
        title="BSIMM12 2021 Foundations Report",
        description="The Building Security In Maturity Model, twelfth edition.")
    CNCFSSCP = PermissibleValue(
        text="CNCFSSCP",
        title="Software Supply Chain Best Practices (2021)",
        description="The Cloud Native Computing Foundation's software supply chain paper.")
    EO14028 = PermissibleValue(
        text="EO14028",
        title="Executive Order 14028, Improving the Nation's Cybersecurity (2021)",
        description="The executive order whose Section 4e clauses SP 800-218 maps in its Appendix A.")
    IDASOAR = PermissibleValue(
        text="IDASOAR",
        title="State-of-the-Art Resources (SOAR) for Software Vulnerability Detection, Test, and Evaluation 2016",
        description="The Institute for Defense Analyses report on software vulnerability tools and techniques.")
    IEC62443 = PermissibleValue(
        text="IEC62443",
        title="IEC 62443-4-1:2018, Secure product development lifecycle requirements",
        description="""The International Electrotechnical Commission's standard for secure development of industrial automation and control products.""")
    IR8397 = PermissibleValue(
        text="IR8397",
        title="NIST IR 8397, Guidelines on Minimum Standards for Developer Verification of Software (2021)",
        description="NIST's guidelines for the verification a software developer performs.")
    ISO27034 = PermissibleValue(
        text="ISO27034",
        title="ISO/IEC 27034-1:2011, Application security, Part 1",
        description="The international standard's overview and concepts of application security.")
    ISO29147 = PermissibleValue(
        text="ISO29147",
        title="ISO/IEC 29147:2018, Vulnerability disclosure",
        description="The international standard for disclosing vulnerabilities in products and services.")
    ISO30111 = PermissibleValue(
        text="ISO30111",
        title="ISO/IEC 30111:2019, Vulnerability handling processes",
        description="The international standard for the processes that handle a reported vulnerability.")
    MSSDL = PermissibleValue(
        text="MSSDL",
        title="Microsoft Security Development Lifecycle (2021)",
        description="Microsoft's practices for building security into software development.")
    NISTCSF = PermissibleValue(
        text="NISTCSF",
        title="Framework for Improving Critical Infrastructure Cybersecurity, version 1.1 (2018)",
        description="The NIST Cybersecurity Framework at version 1.1, which SP 800-218 maps to by subcategory.")
    NISTLABEL = PermissibleValue(
        text="NISTLABEL",
        title="Recommended Criteria for Cybersecurity Labeling of Consumer Software (2022)",
        description="NIST's criteria for a cybersecurity label on consumer software.")
    NTIASBOM = PermissibleValue(
        text="NTIASBOM",
        title="The Minimum Elements For a Software Bill of Materials (2021)",
        description="""The National Telecommunications and Information Administration's minimum elements of a software bill of materials.""")
    OWASPASVS = PermissibleValue(
        text="OWASPASVS",
        title="OWASP Application Security Verification Standard 4.0.3 (2021)",
        description="The Open Web Application Security Project's verification standard for applications.")
    OWASPMASVS = PermissibleValue(
        text="OWASPMASVS",
        title="OWASP Mobile Application Security Verification Standard, version 1.4.2 (2021)",
        description="The Open Web Application Security Project's verification standard for mobile applications.")
    OWASPSAMM = PermissibleValue(
        text="OWASPSAMM",
        title="Software Assurance Maturity Model, version 1.5 (2017)",
        description="The Open Web Application Security Project's software assurance maturity model.")
    OWASPSCVS = PermissibleValue(
        text="OWASPSCVS",
        title="OWASP Software Component Verification Standard, version 1.0 (2020)",
        description="The Open Web Application Security Project's verification standard for software components.")
    PCISSLC = PermissibleValue(
        text="PCISSLC",
        title="Secure Software Lifecycle (Secure SLC) Requirements and Assessment Procedures, version 1.1 (2021)",
        description="""The Payment Card Industry Security Standards Council's requirements for a secure software lifecycle.""")
    SCAGILE = PermissibleValue(
        text="SCAGILE",
        title="Practical Security Stories and Security Tasks for Agile Development Environments (2012)",
        description="SAFECode's security stories and tasks for agile teams.")
    SCFPSSD = PermissibleValue(
        text="SCFPSSD",
        title="Fundamental Practices for Secure Software Development, third edition (2018)",
        description="SAFECode's essential elements of a secure development lifecycle program.")
    SCSIC = PermissibleValue(
        text="SCSIC",
        title="Software Integrity Controls: An Assurance-Based Approach to Minimizing Risks in the Software Supply Chain (2010)",
        description="SAFECode's controls for software integrity in the supply chain.")
    SCTPC = PermissibleValue(
        text="SCTPC",
        title="Managing Security Risks Inherent in the Use of Third-Party Components (2017)",
        description="SAFECode's guidance on the security risks of third-party components.")
    SCTTM = PermissibleValue(
        text="SCTTM",
        title="Tactical Threat Modeling (2017)",
        description="SAFECode's guidance on threat modeling during development.")
    SP800160 = PermissibleValue(
        text="SP800160",
        title="NIST SP 800-160 Volume 1, Systems Security Engineering (2016, updated 2018)",
        description="NIST's considerations for engineering trustworthy secure systems.")
    SP800161 = PermissibleValue(
        text="SP800161",
        title="NIST SP 800-161 Rev. 1 second draft, Cybersecurity Supply Chain Risk Management Practices (2021)",
        description="NIST's supply chain risk management practices, at the draft SP 800-218 cites.")
    SP800181 = PermissibleValue(
        text="SP800181",
        title="NIST SP 800-181, NICE Cybersecurity Workforce Framework (2017)",
        description="The workforce framework whose tasks, knowledge, skills and abilities SP 800-218 maps to.")
    SP800216 = PermissibleValue(
        text="SP800216",
        title="NIST SP 800-216 draft, Recommendations for Federal Vulnerability Disclosure Guidelines (2021)",
        description="NIST's recommendations for federal vulnerability disclosure, at the draft SP 800-218 cites.")
    SP80053 = PermissibleValue(
        text="SP80053",
        title="NIST SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations (2020)",
        description="NIST's catalog of security and privacy controls, which SP 800-218 maps to by control.")

    _defn = EnumDefinition(
        name="SsdfReferenceDocument",
        description="""The established secure development documents that SP 800-218 maps its tasks to, by the labels its References list gives them. SP 800-218 cites each at the edition shown in its title.""",
    )

# Slots
class slots:
    pass

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_218.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_SP_800_218.description, domain=None, range=Optional[str])

slots.ssdfFramework__ssdf_version = Slot(uri=NIST_SP_800_218.ssdf_version, name="ssdfFramework__ssdf_version", curie=NIST_SP_800_218.curie('ssdf_version'),
                   model_uri=NIST_SP_800_218.ssdfFramework__ssdf_version, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+\.[0-9]+$'))

slots.ssdfFramework__practice_groups = Slot(uri=NIST_SP_800_218.practice_groups, name="ssdfFramework__practice_groups", curie=NIST_SP_800_218.curie('practice_groups'),
                   model_uri=NIST_SP_800_218.ssdfFramework__practice_groups, domain=None, range=Union[Union[dict, SsdfPracticeGroup], list[Union[dict, SsdfPracticeGroup]]])

slots.ssdfPracticeGroup__group_id = Slot(uri=NIST_SP_800_218.group_id, name="ssdfPracticeGroup__group_id", curie=NIST_SP_800_218.curie('group_id'),
                   model_uri=NIST_SP_800_218.ssdfPracticeGroup__group_id, domain=None, range=Union[str, SsdfGroupIdentifier])

slots.ssdfPracticeGroup__group_practices = Slot(uri=NIST_SP_800_218.group_practices, name="ssdfPracticeGroup__group_practices", curie=NIST_SP_800_218.curie('group_practices'),
                   model_uri=NIST_SP_800_218.ssdfPracticeGroup__group_practices, domain=None, range=Optional[Union[Union[dict, SsdfPractice], list[Union[dict, SsdfPractice]]]])

slots.ssdfPractice__practice_id = Slot(uri=NIST_SP_800_218.practice_id, name="ssdfPractice__practice_id", curie=NIST_SP_800_218.curie('practice_id'),
                   model_uri=NIST_SP_800_218.ssdfPractice__practice_id, domain=None, range=Union[str, SsdfPracticeIdentifier])

slots.ssdfPractice__practice_tasks = Slot(uri=NIST_SP_800_218.practice_tasks, name="ssdfPractice__practice_tasks", curie=NIST_SP_800_218.curie('practice_tasks'),
                   model_uri=NIST_SP_800_218.ssdfPractice__practice_tasks, domain=None, range=Optional[Union[Union[dict, SsdfTask], list[Union[dict, SsdfTask]]]])

slots.ssdfTask__task_id = Slot(uri=NIST_SP_800_218.task_id, name="ssdfTask__task_id", curie=NIST_SP_800_218.curie('task_id'),
                   model_uri=NIST_SP_800_218.ssdfTask__task_id, domain=None, range=Union[str, SsdfTaskIdentifier])

slots.ssdfTask__former_task_ids = Slot(uri=NIST_SP_800_218.former_task_ids, name="ssdfTask__former_task_ids", curie=NIST_SP_800_218.curie('former_task_ids'),
                   model_uri=NIST_SP_800_218.ssdfTask__former_task_ids, domain=None, range=Optional[Union[Union[str, SsdfTaskIdentifier], list[Union[str, SsdfTaskIdentifier]]]])

slots.ssdfTask__implementation_examples = Slot(uri=NIST_SP_800_218.implementation_examples, name="ssdfTask__implementation_examples", curie=NIST_SP_800_218.curie('implementation_examples'),
                   model_uri=NIST_SP_800_218.ssdfTask__implementation_examples, domain=None, range=Optional[Union[Union[dict, SsdfImplementationExample], list[Union[dict, SsdfImplementationExample]]]])

slots.ssdfTask__task_references = Slot(uri=NIST_SP_800_218.task_references, name="ssdfTask__task_references", curie=NIST_SP_800_218.curie('task_references'),
                   model_uri=NIST_SP_800_218.ssdfTask__task_references, domain=None, range=Optional[Union[Union[dict, SsdfReference], list[Union[dict, SsdfReference]]]])

slots.ssdfImplementationExample__example_id = Slot(uri=NIST_SP_800_218.example_id, name="ssdfImplementationExample__example_id", curie=NIST_SP_800_218.curie('example_id'),
                   model_uri=NIST_SP_800_218.ssdfImplementationExample__example_id, domain=None, range=Union[str, SsdfExampleIdentifier])

slots.ssdfReference__reference_document = Slot(uri=NIST_SP_800_218.reference_document, name="ssdfReference__reference_document", curie=NIST_SP_800_218.curie('reference_document'),
                   model_uri=NIST_SP_800_218.ssdfReference__reference_document, domain=None, range=Union[str, "SsdfReferenceDocument"])

slots.ssdfReference__mapped_items = Slot(uri=NIST_SP_800_218.mapped_items, name="ssdfReference__mapped_items", curie=NIST_SP_800_218.curie('mapped_items'),
                   model_uri=NIST_SP_800_218.ssdfReference__mapped_items, domain=None, range=str,
                   pattern=re.compile(r'\S'))

slots.SsdfImplementationExample_description = Slot(uri=SCHEMA.description, name="SsdfImplementationExample_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_SP_800_218.SsdfImplementationExample_description, domain=SsdfImplementationExample, range=str)
