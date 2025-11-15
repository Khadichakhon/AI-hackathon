"""
Advanced ARC Solver - Comprehensive pattern detection and transformation
Designed to win the Mizzou AGI Hackathon 2025
"""
import json
import numpy as np
from collections import defaultdict, Counter
import copy

# Try to import scipy, fallback to manual implementation
try:
    from scipy.ndimage import label
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    
    def label(input, structure=None):
        """Manual label implementation if scipy not available"""
        arr = np.array(input)
        h, w = arr.shape
        labeled = np.zeros_like(arr, dtype=int)
        visited = set()
        label_id = 1
        
        def dfs(r, c, val, lid):
            if (r, c) in visited or r < 0 or r >= h or c < 0 or c >= w:
                return
            if arr[r, c] != val:
                return
            visited.add((r, c))
            labeled[r, c] = lid
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc, val, lid)
        
        for r in range(h):
            for c in range(w):
                if arr[r, c] != 0 and (r, c) not in visited:
                    dfs(r, c, arr[r, c], label_id)
                    label_id += 1
        
        return labeled, label_id - 1


class AdvancedARCSolver:
    """Advanced solver with multiple pattern detection strategies"""
    
    def __init__(self):
        self.pattern_cache = {}
    
    def solve_task(self, train_data, test_input):
        """Main solving function - tries multiple strategies"""
        if not train_data:
            return test_input
        
        test_arr = np.array(test_input)
        
        # Strategy 1: Try exact geometric transformations
        result = self.try_geometric_transforms(train_data, test_input)
        if result is not None and not np.array_equal(result, test_input):
            return result
        
        # Strategy 2: Try boundary/frame detection
        result = self.try_boundary_patterns(train_data, test_input)
        if result is not None and not np.array_equal(result, test_input):
            return result
        
        # Strategy 3: Try region filling
        result = self.try_region_filling(train_data, test_input)
        if result is not None and not np.array_equal(result, test_input):
            return result
        
        # Strategy 4: Try object manipulation (tip detection, etc.)
        result = self.try_object_manipulation(train_data, test_input)
        if result is not None and not np.array_equal(result, test_input):
            return result
        
        # Strategy 5: Try color-based transformations
        result = self.try_color_transformations(train_data, test_input)
        if result is not None and not np.array_equal(result, test_input):
            return result
        
        # Strategy 6: Try pattern-specific transformations (example01-style)
        result = self.try_pattern_specific(train_data, test_input)
        if result is not None and not np.array_equal(result, test_input):
            return result
        
        # Fallback: return input unchanged
        return test_input
    
    def try_pattern_specific(self, train_data, test_input):
        """Try pattern-specific transformations for complex tasks like example01"""
        test_arr = np.array(test_input)
        
        # Check if this matches example01 pattern (tip manipulation)
        # Look for patterns where objects are transformed but not simple geometric transforms
        transformations = []
        
        for example in train_data:
            input_arr = np.array(example['input'])
            output_arr = np.array(example['output'])
            
            # Check if shapes are similar but transformed
            input_nonzero = np.argwhere(input_arr != 0)
            output_nonzero = np.argwhere(output_arr != 0)
            
            if len(input_nonzero) == len(output_nonzero):
                # Same number of non-zero pixels - might be a transformation
                # Try to find if it's a flip/rotation
                if np.array_equal(np.flipud(input_arr), output_arr):
                    transformations.append('flip_vertical')
                elif np.array_equal(np.fliplr(input_arr), output_arr):
                    transformations.append('flip_horizontal')
                elif np.array_equal(np.rot90(input_arr, 1), output_arr):
                    transformations.append('rotate_90')
                elif np.array_equal(np.rot90(input_arr, 2), output_arr):
                    transformations.append('rotate_180')
                elif np.array_equal(np.rot90(input_arr, 3), output_arr):
                    transformations.append('rotate_270')
        
        # Use most common transformation
        if transformations:
            most_common = Counter(transformations).most_common(1)[0][0]
            
            if most_common == 'flip_vertical':
                return np.flipud(test_arr).tolist()
            elif most_common == 'flip_horizontal':
                return np.fliplr(test_arr).tolist()
            elif most_common == 'rotate_90':
                return np.rot90(test_arr, 1).tolist()
            elif most_common == 'rotate_180':
                return np.rot90(test_arr, 2).tolist()
            elif most_common == 'rotate_270':
                return np.rot90(test_arr, 3).tolist()
        
        return None
    
    def try_geometric_transforms(self, train_data, test_input):
        """Try simple geometric transformations"""
        test_arr = np.array(test_input)
        transformations = []
        
        for example in train_data:
            input_arr = np.array(example['input'])
            output_arr = np.array(example['output'])
            
            # Check various transformations
            if np.array_equal(np.flipud(input_arr), output_arr):
                transformations.append(('flip_vertical', 1))
            elif np.array_equal(np.fliplr(input_arr), output_arr):
                transformations.append(('flip_horizontal', 1))
            elif np.array_equal(np.flipud(np.fliplr(input_arr)), output_arr):
                transformations.append(('flip_both', 1))
            elif np.array_equal(np.rot90(input_arr, 1), output_arr):
                transformations.append(('rotate_90', 1))
            elif np.array_equal(np.rot90(input_arr, 2), output_arr):
                transformations.append(('rotate_180', 1))
            elif np.array_equal(np.rot90(input_arr, 3), output_arr):
                transformations.append(('rotate_270', 1))
            elif np.array_equal(np.transpose(input_arr), output_arr):
                transformations.append(('transpose', 1))
        
        if transformations:
            # Use most common transformation
            transform_counts = defaultdict(int)
            for trans, _ in transformations:
                transform_counts[trans] += 1
            
            best_transform = max(transform_counts, key=transform_counts.get)
            
            # Apply transformation
            if best_transform == 'flip_vertical':
                return np.flipud(test_arr).tolist()
            elif best_transform == 'flip_horizontal':
                return np.fliplr(test_arr).tolist()
            elif best_transform == 'flip_both':
                return np.flipud(np.fliplr(test_arr)).tolist()
            elif best_transform == 'rotate_90':
                return np.rot90(test_arr, 1).tolist()
            elif best_transform == 'rotate_180':
                return np.rot90(test_arr, 2).tolist()
            elif best_transform == 'rotate_270':
                return np.rot90(test_arr, 3).tolist()
            elif best_transform == 'transpose':
                return np.transpose(test_arr).tolist()
        
        return None
    
    def try_boundary_patterns(self, train_data, test_input):
        """Detect boundary/frame drawing patterns (like example02)"""
        test_arr = np.array(test_input)
        
        # Analyze if pattern is about drawing rectangles/frames
        all_match = True
        frame_patterns = []
        
        for example in train_data:
            input_arr = np.array(example['input'])
            output_arr = np.array(example['output'])
            
            # Check if output is a frame around input objects
            input_nonzero = np.argwhere(input_arr != 0)
            if len(input_nonzero) == 0:
                all_match = False
                break
            
            # Get bounding box
            min_r, min_c = input_nonzero.min(axis=0)
            max_r, max_c = input_nonzero.max(axis=0)
            
            # Check if output is a frame
            output_copy = output_arr.copy()
            # Fill interior with background
            if max_r > min_r and max_c > min_c:
                output_copy[min_r+1:max_r, min_c+1:max_c] = 0
            
            # Check if frame matches pattern
            frame_color = None
            if len(input_nonzero) > 0:
                # Get a non-zero color from input
                frame_color = input_arr[input_nonzero[0, 0], input_nonzero[0, 1]]
            
            if frame_color and self.is_frame_pattern(input_arr, output_arr, min_r, min_c, max_r, max_c, frame_color):
                frame_patterns.append((min_r, min_c, max_r, max_c, frame_color))
            else:
                all_match = False
                break
        
        if all_match and frame_patterns:
            # Draw frame for test input
            test_nonzero = np.argwhere(test_arr != 0)
            if len(test_nonzero) > 0:
                min_r, min_c = test_nonzero.min(axis=0)
                max_r, max_c = test_nonzero.max(axis=0)
                
                # Get frame color from first pattern
                frame_color = frame_patterns[0][4]
                
                # Create frame
                result = np.zeros_like(test_arr)
                h, w = test_arr.shape
                
                # Draw vertical lines
                result[min_r:max_r+1, min_c] = frame_color
                result[min_r:max_r+1, max_c] = frame_color
                
                # Draw horizontal lines
                result[min_r, min_c:max_c+1] = frame_color
                result[max_r, min_c:max_c+1] = frame_color
                
                return result.tolist()
        
        return None
    
    def is_frame_pattern(self, input_arr, output_arr, min_r, min_c, max_r, max_c, frame_color):
        """Check if output is a frame pattern"""
        h, w = output_arr.shape
        
        # Check if vertical lines match
        left_col_match = np.all(output_arr[min_r:max_r+1, min_c] == frame_color)
        right_col_match = np.all(output_arr[min_r:max_r+1, max_c] == frame_color)
        
        # Check if horizontal lines match
        top_row_match = np.all(output_arr[min_r, min_c:max_c+1] == frame_color)
        bottom_row_match = np.all(output_arr[max_r, min_c:max_c+1] == frame_color)
        
        return left_col_match and right_col_match and top_row_match and bottom_row_match
    
    def try_region_filling(self, train_data, test_input):
        """Try region filling patterns (like example03, example05)"""
        test_arr = np.array(test_input)
        
        # Analyze color filling patterns
        fill_rules = []
        
        for example in train_data:
            input_arr = np.array(example['input'])
            output_arr = np.array(example['output'])
            
            # Find regions that were filled
            diff = output_arr - input_arr
            filled_pixels = np.argwhere(diff != 0)
            
            if len(filled_pixels) > 0:
                fill_color = output_arr[filled_pixels[0, 0], filled_pixels[0, 1]]
                
                # Try to detect fill rule
                rule = self.detect_fill_rule(input_arr, output_arr, fill_color)
                if rule:
                    fill_rules.append(rule)
        
        if len(fill_rules) == len(train_data):
            # All examples follow same pattern
            best_rule = max(set(fill_rules), key=fill_rules.count)
            return self.apply_fill_rule(test_arr, best_rule)
        
        return None
    
    def detect_fill_rule(self, input_arr, output_arr, fill_color):
        """Detect what rule was used to fill regions"""
        h, w = input_arr.shape
        
        # Rule 1: Fill entire rows/columns that contain specific colors
        # Check if filled regions are entire rows/columns
        diff = (output_arr != input_arr) & (output_arr == fill_color)
        
        # Check rows
        rows_filled = []
        for r in range(h):
            if np.any(diff[r, :]):
                if np.all(diff[r, :] | (input_arr[r, :] != 0)):
                    rows_filled.append(r)
        
        if len(rows_filled) > 0:
            return ('fill_rows', fill_color)
        
        # Check columns
        cols_filled = []
        for c in range(w):
            if np.any(diff[:, c]):
                if np.all(diff[:, c] | (input_arr[:, c] != 0)):
                    cols_filled.append(c)
        
        if len(cols_filled) > 0:
            return ('fill_cols', fill_color)
        
        # Rule 2: Fill regions touching boundaries
        boundary_touching = self.check_boundary_touching(input_arr, diff)
        if boundary_touching:
            return ('fill_boundary_touching', fill_color)
        
        # Rule 3: Fill based on specific color presence
        # Check if fill happens where certain colors exist
        target_colors = np.unique(input_arr[input_arr != 0])
        for color in target_colors:
            color_positions = input_arr == color
            fill_positions = diff & color_positions
            if np.any(fill_positions):
                # Might be filling regions containing this color
                return ('fill_color_regions', fill_color, color)
        
        return None
    
    def check_boundary_touching(self, input_arr, fill_mask):
        """Check if filled regions touch boundaries"""
        h, w = input_arr.shape
        
        # Check top/bottom boundaries
        if np.any(fill_mask[0, :]) or np.any(fill_mask[h-1, :]):
            return True
        
        # Check left/right boundaries
        if np.any(fill_mask[:, 0]) or np.any(fill_mask[:, w-1]):
            return True
        
        return False
    
    def apply_fill_rule(self, test_arr, rule):
        """Apply fill rule to test input"""
        result = test_arr.copy()
        h, w = test_arr.shape
        
        rule_type = rule[0]
        fill_color = rule[1]
        
        if rule_type == 'fill_rows':
            # Fill rows containing non-zero pixels
            for r in range(h):
                if np.any(test_arr[r, :] != 0):
                    result[r, :] = fill_color
        
        elif rule_type == 'fill_cols':
            # Fill columns containing non-zero pixels
            for c in range(w):
                if np.any(test_arr[:, c] != 0):
                    result[:, c] = fill_color
        
        elif rule_type == 'fill_boundary_touching':
            # Fill regions touching boundaries
            # Use connected components
            for color in np.unique(test_arr[test_arr != 0]):
                color_mask = test_arr == color
                labeled, num_features = label(color_mask)
                
                for i in range(1, num_features + 1):
                    obj_mask = labeled == i
                    # Check if touches boundary
                    if (np.any(obj_mask[0, :]) or np.any(obj_mask[h-1, :]) or
                        np.any(obj_mask[:, 0]) or np.any(obj_mask[:, w-1])):
                        result[obj_mask] = fill_color
        
        elif rule_type == 'fill_color_regions':
            # Fill regions containing specific color
            if len(rule) > 2:
                target_color = rule[2]
                result[test_arr == target_color] = fill_color
        
        return result.tolist()
    
    def try_object_manipulation(self, train_data, test_input):
        """Try object manipulation patterns (tip detection, etc.)"""
        test_arr = np.array(test_input)
        
        # Analyze if pattern involves finding tips/extremities
        tip_patterns = []
        
        for example in train_data:
            input_arr = np.array(example['input'])
            output_arr = np.array(example['output'])
            
            # Check if this is a tip manipulation pattern
            pattern = self.detect_tip_pattern(input_arr, output_arr)
            if pattern:
                tip_patterns.append(pattern)
        
        if len(tip_patterns) == len(train_data) and len(tip_patterns) > 0:
            # Apply most common pattern
            best_pattern = max(set(tip_patterns), key=tip_patterns.count)
            return self.apply_tip_pattern(test_arr, best_pattern)
        
        return None
    
    def detect_tip_pattern(self, input_arr, output_arr):
        """Detect tip manipulation patterns"""
        # Find objects in input
        for color in np.unique(input_arr[input_arr != 0]):
            input_mask = input_arr == color
            output_mask = output_arr == color
            
            # Find connected components
            labeled, num_features = label(input_mask)
            
            for i in range(1, num_features + 1):
                obj_mask = labeled == i
                obj_pixels = np.argwhere(obj_mask)
                
                if len(obj_pixels) > 1:
                    # Find tip (point with fewest neighbors)
                    tip_pos = self.find_tip(obj_pixels, input_arr.shape)
                    
                    if tip_pos is not None:
                        # Check what happened to tip in output
                        if output_mask[tip_pos[0], tip_pos[1]]:
                            # Tip remains, might be rotating/flipping tip direction
                            return 'preserve_tip'
                        else:
                            # Tip removed, might be inverting tip
                            return 'invert_tip'
        
        return None
    
    def find_tip(self, pixels, shape):
        """Find tip of an object (pixel with fewest neighbors)"""
        h, w = shape
        min_neighbors = float('inf')
        tip_pos = None
        
        for r, c in pixels:
            neighbors = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    if (nr, nc) in [(p[0], p[1]) for p in pixels]:
                        neighbors += 1
            
            if neighbors < min_neighbors:
                min_neighbors = neighbors
                tip_pos = (r, c)
        
        return tip_pos if min_neighbors <= 2 else None
    
    def apply_tip_pattern(self, test_arr, pattern):
        """Apply tip pattern to test input"""
        result = test_arr.copy()
        
        if pattern == 'invert_tip':
            # Find and manipulate tips
            for color in np.unique(test_arr[test_arr != 0]):
                color_mask = test_arr == color
                labeled, num_features = label(color_mask)
                
                for i in range(1, num_features + 1):
                    obj_mask = labeled == i
                    obj_pixels = np.argwhere(obj_mask)
                    
                    if len(obj_pixels) > 1:
                        tip_pos = self.find_tip(obj_pixels, test_arr.shape)
                        if tip_pos:
                            # Extend tip in opposite direction or remove it
                            # This is simplified - actual implementation would need more analysis
                            pass
        
        return result.tolist()
    
    def try_color_transformations(self, train_data, test_input):
        """Try color mapping/transformation patterns"""
        test_arr = np.array(test_input)
        
        # Analyze color mappings
        color_maps = []
        
        for example in train_data:
            input_arr = np.array(example['input'])
            output_arr = np.array(example['output'])
            
            # Find color mapping
            input_colors = np.unique(input_arr[input_arr != 0])
            output_colors = np.unique(output_arr[output_arr != 0])
            
            if len(input_colors) == len(output_colors):
                # Might be a color mapping
                color_map = {}
                for ic in input_colors:
                    # Find corresponding output color
                    ic_positions = input_arr == ic
                    oc_at_positions = output_arr[ic_positions]
                    if len(oc_at_positions) > 0:
                        most_common = np.bincount(oc_at_positions).argmax()
                        if most_common != 0:
                            color_map[ic] = most_common
                
                if len(color_map) > 0:
                    color_maps.append(color_map)
        
        if len(color_maps) == len(train_data):
            # Use most common color map
            # For now, use first one
            color_map = color_maps[0]
            result = test_arr.copy()
            for old_color, new_color in color_map.items():
                result[test_arr == old_color] = new_color
            return result.tolist()
        
        return None


def solve_arc_task(train_data, test_input):
    """Convenience function to solve an ARC task"""
    solver = AdvancedARCSolver()
    return solver.solve_task(train_data, test_input)


if __name__ == "__main__":
    # Test on example01
    with open('example01.json', 'r') as f:
        task_data = json.load(f)
    
    solver = AdvancedARCSolver()
    result = solver.solve_task(task_data['train'], task_data['test'][0]['input'])
    
    print("Test completed")
    print(f"Output shape: {np.array(result).shape}")

