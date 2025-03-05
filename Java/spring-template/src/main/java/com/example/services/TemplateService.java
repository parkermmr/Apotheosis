package com.example.services;

import com.example.models.Template;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Service;

/** The template service */
@Service
public class TemplateService {

  private final Map<String, Template> templates = new HashMap<>();

  public TemplateService() {}

  /**
   * Create a new template
   *
   * @return the created template
   */
  public Template createTemplate() {
    Template template = new Template();
    templates.put(template.getId(), template);
    return template;
  }

  /**
   * Get a template by id
   *
   * @param id the id of the template
   * @return the template
   */
  public Template getTemplate(String id) {
    return templates.get(id);
  }

  /**
   * Update a template by id
   *
   * @param id the id of the template
   * @param template the updated template
   * @return the updated template
   */
  public Template updateTemplate(String id, Template template) {
    templates.put(id, template);
    return template;
  }

  /**
   * Patch a template by id
   *
   * @param id the id of the template
   * @param template the updated template
   * @return the updated template
   */
  public Template patchTemplate(String id, Template template) {
    Template existing = templates.get(id);
    if (template.getId() != null) {
      existing.setId(template.getId());
    }
    return existing;
  }

  /**
   * Delete a template by id
   *
   * @param id the id of the template
   */
  public void deleteTemplate(String id) {
    templates.remove(id);
  }

  /**
   * Get all templates
   *
   * @return the templates
   */
  public Collection<Template> getTemplates() {
    return templates.values();
  }
}
