export enum Shelves {
  READING = 'Reading',
  READ = 'Read',
  TO_READ = 'To Read'
}

export const shelfValues = {
  [Shelves.READING]: 'currently-reading',
  [Shelves.READ]: 'read',
  [Shelves.TO_READ]: 'to-read',
};
