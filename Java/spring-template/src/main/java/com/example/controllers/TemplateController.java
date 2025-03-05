package com.example.controllers;

import com.example.models.Template;
import com.example.services.TemplateService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * TemplateController
 *
 * <p>This class is the controller for the Template API.
 */
@RestController
@RequestMapping("/api/v1/template")
@Tag(name = "Template", description = "The Template API")
public class TemplateController {

  private final TemplateService templateService;

  /**
   * Constructor
   *
   * @param templateService The service to use for the controller
   */
  public TemplateController(TemplateService templateService) {
    this.templateService = templateService;
  }

  /**
   * Create a new template
   *
   * @return The created template
   */
  @PostMapping
  @Operation(summary = "Create a new template")
  public ResponseEntity<Template> createTemplate() {
    return ResponseEntity.ok(templateService.createTemplate());
  }

  /**
   * Get a template by id
   *
   * @param id The id of the template to get
   * @return The template
   */
  @GetMapping("/{id}")
  @Operation(summary = "Get a template by id")
  public ResponseEntity<Template> getTemplate(@PathVariable String id) {
    return ResponseEntity.ok(templateService.getTemplate(id));
  }

  /**
   * Get all templates
   *
   * @return All templates
   */
  @GetMapping
  @Operation(summary = "Get all templates")
  public ResponseEntity<Iterable<Template>> getTemplates() {
    return ResponseEntity.ok(templateService.getTemplates());
  }

  /**
   * Update a template by id
   *
   * @param id The id of the template to update
   * @param template The template to update
   * @return The updated template
   */
  @PutMapping("/{id}")
  @Operation(summary = "Update a template by id")
  public ResponseEntity<Template> updateTemplate(
      @PathVariable String id, @RequestBody Template template) {
    return ResponseEntity.ok(templateService.updateTemplate(id, template));
  }

  /**
   * Patch a template by id
   *
   * @param id The id of the template to patch
   * @param template The template to patch
   * @return The patched template
   */
  @PatchMapping("/{id}")
  @Operation(summary = "Patch a template by id")
  public ResponseEntity<Template> patchTemplate(
      @PathVariable String id, @RequestBody Template template) {
    return ResponseEntity.ok(templateService.patchTemplate(id, template));
  }

  /**
   * Delete a template by id
   *
   * @param id The id of the template to delete
   * @return The response entity
   */
  @DeleteMapping("/{id}")
  @Operation(summary = "Delete a template by id")
  public ResponseEntity<Void> deleteTemplate(@PathVariable String id) {
    templateService.deleteTemplate(id);
    return ResponseEntity.noContent().build();
  }
}
