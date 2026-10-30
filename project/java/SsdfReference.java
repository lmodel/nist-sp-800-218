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
  A pointer from a task to an established secure development document, and to the parts of that document the task maps to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SsdfReference  {

  private String referenceDocument;
  private String mappedItems;


}