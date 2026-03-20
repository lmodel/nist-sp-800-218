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


metamodel_version = "1.7.0"
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


linkml_meta = LinkMLMeta({'default_prefix': 'nist_sp_800_218',
     'default_range': 'string',
     'description': "'Electronic (LinkML) Version of Secure Software Development "
                    'Framework (SSDF): Recommendations for Mitigating the Risk of '
                    "Software Vulnerabilities'",
     'id': 'https://w3id.org/lmodel/nist-sp-800-218',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist-sp-800-218',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_218': {'prefix_prefix': 'nist_sp_800_218',
                                      'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-218/'}},
     'see_also': ['https://lmodel.github.io/nist-sp-800-218'],
     'source': 'https://doi.org/10.6028/NIST.SP.800-218',
     'source_file': 'src/nist_sp_800_218/schema/nist_sp_800_218.yaml',
     'subsets': {'nist_sp_800_218_catalog': {'description': 'NIST SP 800-218 SSDF '
                                                            'Catalog subset for '
                                                            'practice groups, '
                                                            'practices, and tasks',
                                             'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
                                             'name': 'nist_sp_800_218_catalog'}},
     'title': 'nist-sp-800-218'} )

class CatalogElementClassValue(str, Enum):
    """
    Allowed class values for SSDF catalog elements
    """
    group = "group"
    """
    A top-level practice group
    """
    practice = "practice"
    """
    An SSDF practice within a group
    """
    task = "task"
    """
    A task within an SSDF practice
    """



class Role(ConfiguredBaseModel):
    """
    Role definition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })


class CatalogElement(ConfiguredBaseModel):
    """
    Base class for identifiable catalog elements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_218_catalog']} })


class IdentifiedElement(CatalogElement):
    """
    A catalog element with a title and class classification
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog'],
         'slot_usage': {'class': {'name': 'class',
                                  'range': 'CatalogElementClassValue'}}})

    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_218_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_218_catalog']} })


class ControlGroup(IdentifiedElement):
    """
    An SSDF practice group (e.g. PO, PS, PW, RV)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog']})

    controls: Optional[list[Control]] = Field(default=None, description="""List of practices or tasks""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_218_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_218_catalog']} })


class Control(IdentifiedElement):
    """
    An SSDF practice containing tasks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog'],
         'slot_usage': {'controls': {'name': 'controls', 'range': 'Task'}}})

    controls: Optional[list[Task]] = Field(default=None, description="""List of practices or tasks""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_218_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_218_catalog']} })


class Task(IdentifiedElement):
    """
    An SSDF task within a practice
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog']})

    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_218_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_218_catalog']} })


class Property(ConfiguredBaseModel):
    """
    A name-value property with optional namespace
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog']})

    name: Optional[str] = Field(default=None, description="""Name of a property or part""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    value: Optional[str] = Field(default=None, description="""Property value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'], 'in_subset': ['nist_sp_800_218_catalog']} })
    ns: Optional[str] = Field(default=None, description="""Namespace URI for a property""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'], 'in_subset': ['nist_sp_800_218_catalog']} })


class Link(ConfiguredBaseModel):
    """
    Relationship link with optional annotation text
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog']})

    href: Optional[str] = Field(default=None, description="""Link or resource reference URI""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink', 'Link'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    rel: Optional[str] = Field(default=None, description="""Relationship type for a link""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link'], 'in_subset': ['nist_sp_800_218_catalog']} })
    text: Optional[str] = Field(default=None, description="""Citation or link annotation text""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation', 'Link'], 'in_subset': ['nist_sp_800_218_catalog']} })


class Part(IdentifiedElement):
    """
    Structured narrative part containing prose content
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-218',
         'in_subset': ['nist_sp_800_218_catalog']})

    name: Optional[str] = Field(default=None, description="""Name of a property or part""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    prose: Optional[str] = Field(default=None, description="""Free-text prose content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Part'], 'in_subset': ['nist_sp_800_218_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_218_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_218_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_218_catalog']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Role.model_rebuild()
CatalogElement.model_rebuild()
IdentifiedElement.model_rebuild()
ControlGroup.model_rebuild()
Control.model_rebuild()
Task.model_rebuild()
Property.model_rebuild()
Link.model_rebuild()
Part.model_rebuild()
