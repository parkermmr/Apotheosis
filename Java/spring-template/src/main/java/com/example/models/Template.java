package com.example.models;

import java.util.UUID;

/** Template model class */
public class Template {

  private String Id;

  /** Default constructor */
  public Template() {
    this.Id = UUID.randomUUID().toString();
  }

  /**
   * Constructor with parameters
   *
   * @param id
   */
  public String getId() {
    return Id;
  }

  /**
   * Set the id
   *
   * @param id
   */
  public void setId(String id) {
    Id = id;
  }
}
