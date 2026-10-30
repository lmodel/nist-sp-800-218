package example;

/* metamodel_version: 1.12.0 */
/* version: 1.1.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An action that may be needed to perform a practice, with notional examples of how it could be implemented and references to the documents whose practices it maps to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SsdfTask  {

  private String description;
  private String taskId;
  private List<String> formerTaskIds;
  private List<SsdfImplementationExample> implementationExamples;
  private List<SsdfReference> taskReferences;


}