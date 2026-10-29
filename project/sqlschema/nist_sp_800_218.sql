-- # Class: SsdfFramework Description: One version of the SSDF as a whole: its practice groups, each holding its practices and their tasks.
--     * Slot: id
--     * Slot: ssdf_version Description: The SSDF version, as NIST numbers it in the publication's title, such as 1.1.
-- # Class: SsdfPracticeGroup Description: One of the four groups SP 800-218 sorts its practices into: preparing the organization, protecting the software, producing well-secured software, and responding to vulnerabilities.
--     * Slot: id
--     * Slot: title Description: The name SP 800-218 gives the practice group or practice.
--     * Slot: description Description: What the practice group, practice, task or example says, in the words of whoever records it.
--     * Slot: group_id Description: The group's two letters, such as PO for Prepare the Organization.
--     * Slot: SsdfFramework_id Description: Autocreated FK slot
-- # Class: SsdfPractice Description: A secure software development practice: a named outcome with an identifier, a short explanation of what it is and why it helps, and the tasks that may be needed to achieve it.
--     * Slot: id
--     * Slot: title Description: The name SP 800-218 gives the practice group or practice.
--     * Slot: description Description: What the practice group, practice, task or example says, in the words of whoever records it.
--     * Slot: practice_id Description: The practice's identifier, such as PO.1.
--     * Slot: SsdfPracticeGroup_id Description: Autocreated FK slot
-- # Class: SsdfTask Description: An action that may be needed to perform a practice, with notional examples of how it could be implemented and references to the documents whose practices it maps to.
--     * Slot: id
--     * Slot: description Description: What the practice group, practice, task or example says, in the words of whoever records it.
--     * Slot: task_id Description: The task's identifier, such as PO.1.1.
--     * Slot: SsdfPractice_id Description: Autocreated FK slot
-- # Class: SsdfImplementationExample Description: A notional implementation example: one type of tool, process or other method that could help implement a task.
--     * Slot: id
--     * Slot: description Description: What the practice group, practice, task or example says, in the words of whoever records it.
--     * Slot: example_id Description: The example's identifier in NIST's reference data, such as PO.1.1.1 for the first example of task PO.1.1.
--     * Slot: SsdfTask_id Description: Autocreated FK slot
-- # Class: SsdfReference Description: A pointer from a task to an established secure development document, and to the parts of that document the task maps to.
--     * Slot: id
--     * Slot: reference_document Description: The document the task maps to, by the label SP 800-218 gives it.
--     * Slot: mapped_items Description: The parts of the document the task maps to, as SP 800-218 lists them, such as the clause, control or activity identifiers SM.3, DE.1.
--     * Slot: SsdfTask_id Description: Autocreated FK slot
-- # Class: SsdfTask_former_task_ids
--     * Slot: SsdfTask_id Description: Autocreated FK slot
--     * Slot: former_task_ids Description: The identifiers the task had in an earlier SSDF version, which SP 800-218 notes beside the task after moving it, such as PW.3.1 for PO.1.3.

CREATE TABLE "SsdfFramework" (
	id INTEGER NOT NULL,
	ssdf_version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SsdfFramework_id" ON "SsdfFramework" (id);

CREATE TABLE "SsdfPracticeGroup" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	group_id TEXT NOT NULL,
	"SsdfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SsdfFramework_id") REFERENCES "SsdfFramework" (id)
);
CREATE INDEX "ix_SsdfPracticeGroup_id" ON "SsdfPracticeGroup" (id);

CREATE TABLE "SsdfPractice" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	practice_id TEXT NOT NULL,
	"SsdfPracticeGroup_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SsdfPracticeGroup_id") REFERENCES "SsdfPracticeGroup" (id)
);
CREATE INDEX "ix_SsdfPractice_id" ON "SsdfPractice" (id);

CREATE TABLE "SsdfTask" (
	id INTEGER NOT NULL,
	description TEXT,
	task_id TEXT NOT NULL,
	"SsdfPractice_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SsdfPractice_id") REFERENCES "SsdfPractice" (id)
);
CREATE INDEX "ix_SsdfTask_id" ON "SsdfTask" (id);

CREATE TABLE "SsdfImplementationExample" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	example_id TEXT NOT NULL,
	"SsdfTask_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SsdfTask_id") REFERENCES "SsdfTask" (id)
);
CREATE INDEX "ix_SsdfImplementationExample_id" ON "SsdfImplementationExample" (id);

CREATE TABLE "SsdfReference" (
	id INTEGER NOT NULL,
	reference_document VARCHAR(10) NOT NULL,
	mapped_items TEXT NOT NULL,
	"SsdfTask_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SsdfTask_id") REFERENCES "SsdfTask" (id)
);
CREATE INDEX "ix_SsdfReference_id" ON "SsdfReference" (id);

CREATE TABLE "SsdfTask_former_task_ids" (
	"SsdfTask_id" INTEGER,
	former_task_ids TEXT,
	PRIMARY KEY ("SsdfTask_id", former_task_ids),
	FOREIGN KEY("SsdfTask_id") REFERENCES "SsdfTask" (id)
);
CREATE INDEX "ix_SsdfTask_former_task_ids_SsdfTask_id" ON "SsdfTask_former_task_ids" ("SsdfTask_id");
CREATE INDEX "ix_SsdfTask_former_task_ids_former_task_ids" ON "SsdfTask_former_task_ids" (former_task_ids);
