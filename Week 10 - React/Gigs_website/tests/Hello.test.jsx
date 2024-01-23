import { screen, render } from "@testing-library/react";

import Hello from "../src/components/Hello";
import Gig from "../src/components/Gig";

describe("Hello", () => {
  it("Should render a h1 with the correct title", () => {
    render(<Hello title="Test title" />);
    expect(screen.getByText("Test title!"));
  });
});

describe("Test gig page", () => {
  it("Should render a band for the gig", () => {
    render(<Gig
      band = 'Nothing But Thieves'
      imageURL = ''
      description = ''
      dateTime = ''
      venue = ''
      />);
    expect(screen.getByText("Nothing But Thieves"));
  });

  it("Should render a description", () => {
    render(<Gig
      band = ''
      imageURL = ''
      description = 'Description of gig'
      dateTime = ''
      venue = ''
      />);
    expect(screen.getByText("Description of gig"));
  });

  it("Should render a gig", () => {
    render(<Gig
      band = 'Nothing But Thieves'
      imageURL = ''
      description = 'Description of gig'
      dateTime = '20/02/24 20:00'
      venue = 'OVO Wembley'
      />);
    const description = document.getElementById('.eventDescription')
    expect(screen.getByText("Nothing But Thieves"));
  });
});
