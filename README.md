# Open Source Games

[Dynamic HTML table](https://trilarion.github.io/opensourcegames/) of the entries / Development [Blog](https://trilarion.blogspot.com/search/label/osgames)

[comment]: # (start of autogenerated content, do not edit)
413 entries
- **[Action/Arcade](games/action/_toc.md)** (21)
- **[Adventure & Visual novels](games/adventure/_toc.md)** (15)
- **[Engines & Frameworks](games/framework/_toc.md)** (52)
- **[Libraries](games/library/_toc.md)** (22)
- **[Role Playing](games/rpg/_toc.md)** (108)
- **[Simulation](games/simulation/_toc.md)** (15)
- **[Strategy](games/strategy/_toc.md)** (167)
- **[Tools & Manuals](games/misc/_toc.md)** (13)

[comment]: # (end of autogenerated content)

A list of open source games sorted by genre. The projects are at least in beta stage with a code basis that builds
into an executable demo. The code must be under a license that allows modification and sharing by others. For each entry,
relevant information is collected regarding code repositories, download possibilities and build instructions.

Similar collections: [Open Source Clones](https://github.com/opengaming/osgameclones)  of Popular Games, Popular games, add-ons, maps, etc.  [hosted on GitHub.](https://github.com/leereilly/games), [List of open-source video games](https://en.wikipedia.org/wiki/List_of_open-source_video_games) on Wikipedia

See also the **[Statistics](games/statistics.md)** page.

## Contributing

If you'd like to add or modify entries, please use the [Issue tracker](https://github.com/Trilarion/opensourcegames/issues),
or fork this repository and submit a pull request.

### Adding a new entry

All entries are stored as markdown (quite human readable) format. Adding a new entry is as easy as modifying the
[template](games/template.md) and putting a modified version in a games category subdirectory.

Here is a description of the fields in the template. Comments start with "//".

<pre>
# {NAME} // name of the game

_{Description}_ // single description line (typically taken from about page of game)

- Home: {URL} // project main site(s) (most significant first)
- Media: {URL} // links to wikipedia and other significant mentions
- State: {XX} // one of {beta, mature} and optional "inactive since YEAR"
- Play: {URL} // link(s) to online play possibility
- Download: {URL} // link(s) to download binary (or source) releases
- Platform: {XX} // list of supported platforms {Linux, Windows, MacOs, Android, ..}
- Keywords: {XX} // list of tags describing the game
- Code repository: {URL} // code repositories (most significant first)
- Code language: {XX} // programming language(s) used 
- Code license: {XX} // license of the code, use "Custom" with comment if the license is modified for the project
- Code dependencies: {XX} // important third party libraries / frameworks used by the project
- Assets license: {XX} // license(s) of the assets (artwork, ..)

// whatever you want to put here

## Building

- Build system: {XX} // typically one of {CMake, Autoconf, Gradle, ..}
- Build instructions: {XX} // link(s) to build instructions offered by the project

// whatever you want to put here
</pre>

- If there are multiple links, licenses, ... separate them by comma.
- The same link can be assigned to different fields (home could also be the code repository, etc.).
- Put comments in "()" parentheses (do not put commas in comments).
- Remove lines with fields that do not apply to the project or where information is not available otherwise.

Help: [MarkDown Help](https://help.github.com/articles/github-flavored-markdown), [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Background

I love open source projects and games and I am currently interested in learning more about building systems.
I see the following benefits of this database and further actions I intend to do.

- General information about open source games
- Possibility of improving build instructions on the projects side (not all projects actually have build instructions)
- Simplifying builds
- Adding infrastructure for automatic testing and deploying where not already present
- Revival of abandoned games that do not build anymore
- Simplifying dependencies
- Increasing the number of supported platforms
- Conversion of old repository formats like CVS to Git

## Disclaimer
 
 No warranty whatsoever of the information presented herein for any purpose. There could be errors in here.

## License

See [LICENSE](LICENSE). You are free to do whatever you want with this repository.
