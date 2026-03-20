# Auto generated from nist_sp_800_218.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-20T15:24:48
# Schema: nist-sp-800-218
#
# id: https://w3id.org/lmodel/nist-sp-800-218
# description: 'Electronic (LinkML) Version of Secure Software Development Framework (SSDF): Recommendations for Mitigating the Risk of Software Vulnerabilities'
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

metamodel_version = "1.7.0"
version = "1.1.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_218 = CurieNamespace('nist_sp_800_218', 'https://w3id.org/lmodel/nist-sp-800-218/')
DEFAULT_ = NIST_SP_800_218


# Types

# Class references



SSFDDocument = Any

CatalogBody = Any

Metadata = Any

@dataclass(repr=False)
class Role(YAMLRoot):
    """
    Role definition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Role"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.Role

    id: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


Party = Any

Address = Any

ResponsibleParty = Any

BackMatter = Any

Resource = Any

Citation = Any

ResourceLink = Any

@dataclass(repr=False)
class CatalogElement(YAMLRoot):
    """
    Base class for identifiable catalog elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["CatalogElement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:CatalogElement"
    class_name: ClassVar[str] = "CatalogElement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.CatalogElement

    id: Optional[str] = None
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if not isinstance(self.props, list):
            self.props = [self.props] if self.props is not None else []
        self.props = [v if isinstance(v, Property) else Property(**as_dict(v)) for v in self.props]

        if not isinstance(self.links, list):
            self.links = [self.links] if self.links is not None else []
        self.links = [v if isinstance(v, Link) else Link(**as_dict(v)) for v in self.links]

        if not isinstance(self.parts, list):
            self.parts = [self.parts] if self.parts is not None else []
        self.parts = [v if isinstance(v, Part) else Part(**as_dict(v)) for v in self.parts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifiedElement(CatalogElement):
    """
    A catalog element with a title and class classification
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["IdentifiedElement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:IdentifiedElement"
    class_name: ClassVar[str] = "IdentifiedElement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.IdentifiedElement

    title: Optional[str] = None
    _class: Optional[Union[str, "CatalogElementClassValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self._class is not None and not isinstance(self._class, CatalogElementClassValue):
            self._class = CatalogElementClassValue(self._class)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlGroup(IdentifiedElement):
    """
    An SSDF practice group (e.g. PO, PS, PW, RV)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["ControlGroup"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:ControlGroup"
    class_name: ClassVar[str] = "ControlGroup"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.ControlGroup

    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, Control) else Control(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Control(IdentifiedElement):
    """
    An SSDF practice containing tasks
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Control"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Control"
    class_name: ClassVar[str] = "Control"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.Control

    controls: Optional[Union[Union[dict, "Task"], list[Union[dict, "Task"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, Task) else Task(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


class Task(IdentifiedElement):
    """
    An SSDF task within a practice
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Task"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.Task


@dataclass(repr=False)
class Property(YAMLRoot):
    """
    A name-value property with optional namespace
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Property"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.Property

    name: Optional[str] = None
    value: Optional[str] = None
    ns: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Link(YAMLRoot):
    """
    Relationship link with optional annotation text
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Link"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Link"
    class_name: ClassVar[str] = "Link"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.Link

    href: Optional[str] = None
    rel: Optional[str] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Part(IdentifiedElement):
    """
    Structured narrative part containing prose content
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_218["Part"]
    class_class_curie: ClassVar[str] = "nist_sp_800_218:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_218.Part

    name: Optional[str] = None
    prose: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        super().__post_init__(**kwargs)


# Enumerations
class CatalogElementClassValue(EnumDefinitionImpl):
    """
    Allowed class values for SSDF catalog elements
    """
    group = PermissibleValue(
        text="group",
        description="A top-level practice group")
    practice = PermissibleValue(
        text="practice",
        description="An SSDF practice within a group")
    task = PermissibleValue(
        text="task",
        description="A task within an SSDF practice")

    _defn = EnumDefinition(
        name="CatalogElementClassValue",
        description="Allowed class values for SSDF catalog elements",
    )

# Slots
class slots:
    pass

slots.catalog = Slot(uri=NIST_SP_800_218.catalog, name="catalog", curie=NIST_SP_800_218.curie('catalog'),
                   model_uri=NIST_SP_800_218.catalog, domain=None, range=Optional[Union[dict, CatalogBody]])

slots.metadata = Slot(uri=NIST_SP_800_218.metadata, name="metadata", curie=NIST_SP_800_218.curie('metadata'),
                   model_uri=NIST_SP_800_218.metadata, domain=None, range=Optional[Union[dict, Metadata]])

slots.groups = Slot(uri=NIST_SP_800_218.groups, name="groups", curie=NIST_SP_800_218.curie('groups'),
                   model_uri=NIST_SP_800_218.groups, domain=None, range=Optional[Union[Union[dict, ControlGroup], list[Union[dict, ControlGroup]]]])

slots.controls = Slot(uri=NIST_SP_800_218.controls, name="controls", curie=NIST_SP_800_218.curie('controls'),
                   model_uri=NIST_SP_800_218.controls, domain=None, range=Optional[Union[Union[dict, Control], list[Union[dict, Control]]]])

slots.props = Slot(uri=NIST_SP_800_218.props, name="props", curie=NIST_SP_800_218.curie('props'),
                   model_uri=NIST_SP_800_218.props, domain=None, range=Optional[Union[Union[dict, Property], list[Union[dict, Property]]]])

slots.links = Slot(uri=NIST_SP_800_218.links, name="links", curie=NIST_SP_800_218.curie('links'),
                   model_uri=NIST_SP_800_218.links, domain=None, range=Optional[Union[Union[dict, Link], list[Union[dict, Link]]]])

slots.parts = Slot(uri=NIST_SP_800_218.parts, name="parts", curie=NIST_SP_800_218.curie('parts'),
                   model_uri=NIST_SP_800_218.parts, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.id = Slot(uri=NIST_SP_800_218.id, name="id", curie=NIST_SP_800_218.curie('id'),
                   model_uri=NIST_SP_800_218.id, domain=None, range=Optional[str])

slots.uuid = Slot(uri=NIST_SP_800_218.uuid, name="uuid", curie=NIST_SP_800_218.curie('uuid'),
                   model_uri=NIST_SP_800_218.uuid, domain=None, range=Optional[str])

slots.title = Slot(uri=NIST_SP_800_218.title, name="title", curie=NIST_SP_800_218.curie('title'),
                   model_uri=NIST_SP_800_218.title, domain=None, range=Optional[str])

slots.version = Slot(uri=NIST_SP_800_218.version, name="version", curie=NIST_SP_800_218.curie('version'),
                   model_uri=NIST_SP_800_218.version, domain=None, range=Optional[str])

slots.published = Slot(uri=NIST_SP_800_218.published, name="published", curie=NIST_SP_800_218.curie('published'),
                   model_uri=NIST_SP_800_218.published, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=NIST_SP_800_218.last_modified, name="last-modified", curie=NIST_SP_800_218.curie('last_modified'),
                   model_uri=NIST_SP_800_218.last_modified, domain=None, range=Optional[str])

slots.oscal_version = Slot(uri=NIST_SP_800_218.oscal_version, name="oscal-version", curie=NIST_SP_800_218.curie('oscal_version'),
                   model_uri=NIST_SP_800_218.oscal_version, domain=None, range=Optional[str])

slots._class = Slot(uri=NIST_SP_800_218._class, name="_class", curie=NIST_SP_800_218.curie('_class'),
                   model_uri=NIST_SP_800_218._class, domain=None, range=Optional[str])

slots.name = Slot(uri=NIST_SP_800_218.name, name="name", curie=NIST_SP_800_218.curie('name'),
                   model_uri=NIST_SP_800_218.name, domain=None, range=Optional[str])

slots.value = Slot(uri=NIST_SP_800_218.value, name="value", curie=NIST_SP_800_218.curie('value'),
                   model_uri=NIST_SP_800_218.value, domain=None, range=Optional[str])

slots.ns = Slot(uri=NIST_SP_800_218.ns, name="ns", curie=NIST_SP_800_218.curie('ns'),
                   model_uri=NIST_SP_800_218.ns, domain=None, range=Optional[str])

slots.prose = Slot(uri=NIST_SP_800_218.prose, name="prose", curie=NIST_SP_800_218.curie('prose'),
                   model_uri=NIST_SP_800_218.prose, domain=None, range=Optional[str])

slots.roles = Slot(uri=NIST_SP_800_218.roles, name="roles", curie=NIST_SP_800_218.curie('roles'),
                   model_uri=NIST_SP_800_218.roles, domain=None, range=Optional[Union[Union[dict, Role], list[Union[dict, Role]]]])

slots.parties = Slot(uri=NIST_SP_800_218.parties, name="parties", curie=NIST_SP_800_218.curie('parties'),
                   model_uri=NIST_SP_800_218.parties, domain=None, range=Optional[Union[Union[dict, Party], list[Union[dict, Party]]]])

slots.responsible_parties = Slot(uri=NIST_SP_800_218.responsible_parties, name="responsible-parties", curie=NIST_SP_800_218.curie('responsible_parties'),
                   model_uri=NIST_SP_800_218.responsible_parties, domain=None, range=Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]])

slots.role_id = Slot(uri=NIST_SP_800_218.role_id, name="role-id", curie=NIST_SP_800_218.curie('role_id'),
                   model_uri=NIST_SP_800_218.role_id, domain=None, range=Optional[str])

slots.party_uuids = Slot(uri=NIST_SP_800_218.party_uuids, name="party-uuids", curie=NIST_SP_800_218.curie('party_uuids'),
                   model_uri=NIST_SP_800_218.party_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.type = Slot(uri=NIST_SP_800_218.type, name="type", curie=NIST_SP_800_218.curie('type'),
                   model_uri=NIST_SP_800_218.type, domain=None, range=Optional[str])

slots.short_name = Slot(uri=NIST_SP_800_218.short_name, name="short-name", curie=NIST_SP_800_218.curie('short_name'),
                   model_uri=NIST_SP_800_218.short_name, domain=None, range=Optional[str])

slots.email_addresses = Slot(uri=NIST_SP_800_218.email_addresses, name="email-addresses", curie=NIST_SP_800_218.curie('email_addresses'),
                   model_uri=NIST_SP_800_218.email_addresses, domain=None, range=Optional[Union[str, list[str]]])

slots.addresses = Slot(uri=NIST_SP_800_218.addresses, name="addresses", curie=NIST_SP_800_218.curie('addresses'),
                   model_uri=NIST_SP_800_218.addresses, domain=None, range=Optional[Union[Union[dict, Address], list[Union[dict, Address]]]])

slots.addr_lines = Slot(uri=NIST_SP_800_218.addr_lines, name="addr-lines", curie=NIST_SP_800_218.curie('addr_lines'),
                   model_uri=NIST_SP_800_218.addr_lines, domain=None, range=Optional[Union[str, list[str]]])

slots.city = Slot(uri=NIST_SP_800_218.city, name="city", curie=NIST_SP_800_218.curie('city'),
                   model_uri=NIST_SP_800_218.city, domain=None, range=Optional[str])

slots.state = Slot(uri=NIST_SP_800_218.state, name="state", curie=NIST_SP_800_218.curie('state'),
                   model_uri=NIST_SP_800_218.state, domain=None, range=Optional[str])

slots.postal_code = Slot(uri=NIST_SP_800_218.postal_code, name="postal-code", curie=NIST_SP_800_218.curie('postal_code'),
                   model_uri=NIST_SP_800_218.postal_code, domain=None, range=Optional[str])

slots.back_matter = Slot(uri=NIST_SP_800_218.back_matter, name="back-matter", curie=NIST_SP_800_218.curie('back_matter'),
                   model_uri=NIST_SP_800_218.back_matter, domain=None, range=Optional[Union[dict, BackMatter]])

slots.resources = Slot(uri=NIST_SP_800_218.resources, name="resources", curie=NIST_SP_800_218.curie('resources'),
                   model_uri=NIST_SP_800_218.resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.citation = Slot(uri=NIST_SP_800_218.citation, name="citation", curie=NIST_SP_800_218.curie('citation'),
                   model_uri=NIST_SP_800_218.citation, domain=None, range=Optional[Union[dict, Citation]])

slots.text = Slot(uri=NIST_SP_800_218.text, name="text", curie=NIST_SP_800_218.curie('text'),
                   model_uri=NIST_SP_800_218.text, domain=None, range=Optional[str])

slots.rlinks = Slot(uri=NIST_SP_800_218.rlinks, name="rlinks", curie=NIST_SP_800_218.curie('rlinks'),
                   model_uri=NIST_SP_800_218.rlinks, domain=None, range=Optional[Union[Union[dict, ResourceLink], list[Union[dict, ResourceLink]]]])

slots.href = Slot(uri=NIST_SP_800_218.href, name="href", curie=NIST_SP_800_218.curie('href'),
                   model_uri=NIST_SP_800_218.href, domain=None, range=Optional[str])

slots.rel = Slot(uri=NIST_SP_800_218.rel, name="rel", curie=NIST_SP_800_218.curie('rel'),
                   model_uri=NIST_SP_800_218.rel, domain=None, range=Optional[str])

slots.IdentifiedElement__class = Slot(uri=NIST_SP_800_218._class, name="IdentifiedElement__class", curie=NIST_SP_800_218.curie('_class'),
                   model_uri=NIST_SP_800_218.IdentifiedElement__class, domain=IdentifiedElement, range=Optional[Union[str, "CatalogElementClassValue"]])

slots.Control_controls = Slot(uri=NIST_SP_800_218.controls, name="Control_controls", curie=NIST_SP_800_218.curie('controls'),
                   model_uri=NIST_SP_800_218.Control_controls, domain=Control, range=Optional[Union[Union[dict, "Task"], list[Union[dict, "Task"]]]])
