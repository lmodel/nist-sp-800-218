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
  One version of the SSDF as a whole: its practice groups, each holding its practices and their tasks.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SsdfFramework  {

  private String ssdfVersion;
  private List<SsdfPracticeGroup> practiceGroups;


}