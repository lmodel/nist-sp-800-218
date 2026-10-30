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
  One of the four groups SP 800-218 sorts its practices into: preparing the organization, protecting the software, producing well-secured software, and responding to vulnerabilities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SsdfPracticeGroup  {

  private String title;
  private String description;
  private String groupId;
  private List<SsdfPractice> groupPractices;


}