/**
* Allowed class values for SSDF catalog elements
*/
export enum CatalogElementClassValue {
    
    /** A top-level practice group */
    group = "group",
    /** An SSDF practice within a group */
    practice = "practice",
    /** A task within an SSDF practice */
    task = "task",
};


/**
 * Root wrapper for SSDF catalog content
 */
export interface SSFDDocument {
    /** Root catalog payload */
    catalog?: CatalogBody,
}


/**
 * Main SSDF catalog object
 */
export interface CatalogBody {
    /** UUID for catalog or resource element */
    uuid?: string,
    /** Catalog metadata */
    metadata?: Metadata,
    /** List of SSDF practice groups in the catalog */
    groups?: ControlGroup[],
    /** Back-matter references and resources */
    back_matter?: BackMatter,
}


/**
 * OSCAL metadata section for the SSDF catalog
 */
export interface Metadata {
    /** Human-readable title */
    title?: string,
    /** Publication timestamp */
    published?: string,
    /** Last modification timestamp */
    last_modified?: string,
    /** Version identifier */
    version?: string,
    /** OSCAL version identifier */
    oscal_version?: string,
    /** List of properties */
    props?: Property[],
    /** List of links and relationships */
    links?: Link[],
    /** Roles used in metadata */
    roles?: Role[],
    /** Parties used in metadata */
    parties?: Party[],
    /** Responsible party assignments */
    responsible_parties?: ResponsibleParty[],
}


/**
 * Role definition
 */
export interface Role {
    /** Unique identifier for an element */
    id?: string,
    /** Human-readable title */
    title?: string,
}


/**
 * Party definition
 */
export interface Party {
    /** UUID for catalog or resource element */
    uuid?: string,
    /** Party type */
    type?: string,
    /** Name of a property or part */
    name?: string,
    /** Short display name */
    short_name?: string,
    /** Party email addresses */
    email_addresses?: string[],
    /** Postal addresses */
    addresses?: Address[],
}


/**
 * Postal address
 */
export interface Address {
    /** Address lines */
    addr_lines?: string[],
    /** City name */
    city?: string,
    /** State or region */
    state?: string,
    /** Postal code */
    postal_code?: string,
}


/**
 * Assignment of parties to a role
 */
export interface ResponsibleParty {
    /** Assigned role identifier */
    role_id?: string,
    /** Referenced party UUIDs */
    party_uuids?: string[],
}


/**
 * OSCAL back-matter section
 */
export interface BackMatter {
    /** Back-matter resources */
    resources?: Resource[],
}


/**
 * Referenced resource in back-matter
 */
export interface Resource {
    /** UUID for catalog or resource element */
    uuid?: string,
    /** Human-readable title */
    title?: string,
    /** Citation details for a resource */
    citation?: Citation,
    /** Resource links */
    rlinks?: ResourceLink[],
}


/**
 * Citation wrapper
 */
export interface Citation {
    /** Citation or link annotation text */
    text?: string,
}


/**
 * Reference link for a resource
 */
export interface ResourceLink {
    /** Link or resource reference URI */
    href?: string,
}


/**
 * Base class for identifiable catalog elements
 */
export interface CatalogElement {
    /** Unique identifier for an element */
    id?: string,
    /** List of properties */
    props?: Property[],
    /** List of links and relationships */
    links?: Link[],
    /** Nested parts that provide prose and structure */
    parts?: Part[],
}


/**
 * A catalog element with a title and class classification
 */
export interface IdentifiedElement extends CatalogElement {
    /** Human-readable title */
    title?: string,
    /** Classification of a catalog element */
    class?: string,
}


/**
 * An SSDF practice group (e.g. PO, PS, PW, RV)
 */
export interface ControlGroup extends IdentifiedElement {
    /** List of practices or tasks */
    controls?: Control[],
}


/**
 * An SSDF practice containing tasks
 */
export interface Control extends IdentifiedElement {
    /** List of practices or tasks */
    controls?: Task[],
}


/**
 * An SSDF task within a practice
 */
export interface Task extends IdentifiedElement {
}


/**
 * A name-value property with optional namespace
 */
export interface Property {
    /** Name of a property or part */
    name?: string,
    /** Property value */
    value?: string,
    /** Namespace URI for a property */
    ns?: string,
}


/**
 * Relationship link with optional annotation text
 */
export interface Link {
    /** Link or resource reference URI */
    href?: string,
    /** Relationship type for a link */
    rel?: string,
    /** Citation or link annotation text */
    text?: string,
}


/**
 * Structured narrative part containing prose content
 */
export interface Part extends IdentifiedElement {
    /** Name of a property or part */
    name?: string,
    /** Free-text prose content */
    prose?: string,
}



