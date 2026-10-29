package None;

/* metamodel_version: 1.7.0 */
/* version: 1.1.0 */
import java.util.List;
import lombok.*;

/**
  A secure software development practice: a named outcome with an identifier, a short explanation of what it is and why it helps, and the tasks that may be needed to achieve it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SsdfPractice  {

  private String title;
  private String description;
  private String practiceId;
  private List<SsdfTask> practiceTasks;

}