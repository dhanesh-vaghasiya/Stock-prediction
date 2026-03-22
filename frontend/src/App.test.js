import { render, screen } from '@testing-library/react';
import App from './App';

test('renders stock predictor title', () => {
  render(<App />);
  expect(screen.getByText(/AI Stock Predictor/i)).toBeInTheDocument();
});
