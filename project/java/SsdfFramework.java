package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
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